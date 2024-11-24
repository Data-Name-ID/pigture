from django_filters import rest_framework as filters
from rest_framework import decorators, permissions, status
from rest_framework.parsers import (
    FormParser,
    JSONParser,
    MultiPartParser,
)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import core.permissions
from core.permissions import is_in_group
from images.models import Image
from images.permissions import IsImageAuthor
from images.serializers import ImageSerializer
from images.tasks import process_image
from marking.serializers import TagSerializer
from notes.serializers import NoteSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all().order_by("-uploaded_at")
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = [core.permissions.HasGroupPermission]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("category", "tags", "patient")

    required_groups = {
        "GET": ["main_docs", "docs"],
        "POST": ["main_docs", "docs", "labs"],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if is_in_group(user, "labs"):
            queryset = queryset.filter(author=user)

        return queryset

    def get_permissions(self):
        if is_in_group(self.request.user, "labs"):
            self.permission_classes = [IsImageAuthor]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        image_instance: Image = serializer.save(author=self.request.user)

        process_image.delay(image_instance.file.path, image_instance.id)

        image_instance.tiles = f"tiles/{image_instance.id}/tiles.dzi"
        image_instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @decorators.action(methods=["get"], detail=True)
    def notes(self, request, pk=None):
        image = self.get_object()
        notes_set = image.notes.all()
        serializer = NoteSerializer(notes_set, many=True)
        return Response(serializer.data)

    @decorators.action(methods=["get"], detail=True)
    def tags(self, request, pk=None):
        image = self.get_object()
        tags_set = image.tags.all()
        serializer = TagSerializer(tags_set, many=True)
        return Response(serializer.data)
