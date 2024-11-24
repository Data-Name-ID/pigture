from rest_framework import status
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
from images.serializers import ImageSerializer
from images.tasks import process_image


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all().order_by("-uploaded_at")
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
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

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        image_instance: Image = serializer.save(author=self.request.user)

        process_image.delay(image_instance.file.path, image_instance.id)

        image_instance.tiles = f"tiles/{image_instance.id}/tiles.dzi"
        image_instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
