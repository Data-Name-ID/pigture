from rest_framework import status, decorators
from rest_framework import permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import core.permissions
from core.permissions import is_in_group
from images.models import Image, Tiles
from images.serializers import ImageSerializer, TilesSerializer
from notes.serializers import NoteSerializer
from marking.serializers import TagSerializer
from images.tasks import process_image
from images.permissions import IsImageAuthor


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all().order_by("-uploaded_at")
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [core.permissions.HasGroupPermission]
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
        serializer = self.serializer_class(
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)

        image_instance = serializer.save()

        process_image.delay(image_instance.file.path, image_instance.id)
        Tiles.objects.create(
            image=image_instance,
            file=f"tiles/{image_instance.id}/tiles.dzi",
        )
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


class TilesViewSet(ModelViewSet):
    queryset = Tiles.objects.all()
    serializer_class = TilesSerializer

    http_method_names = ["get"]
