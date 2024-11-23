from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from images.models import Image
from images.serializers import ImageSerializer
from marking.models import Category, Tag

import core.permissions


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [core.permissions.HasGroupPermission]
    required_groups = {
        "GET": ["main_docs", "docs"],
        "POST": ["main_docs", "docs", "labs"],
    }

    def create(self, request, *args, **kwargs):
        file = request.FILES.get("image")
        if not file:
            return Response(
                {"error": "No file provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        category = None
        category_id = request.data.get("category")
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                return Response(
                    {"error": "Category not found"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        image_instance = Image.objects.create(
            image=file,
            category=category,
            name=request.data.get("name"),
            description=request.data.get("description"),
            metadata=request.data.get("metadata", {}),
        )

        tag_ids = request.data.getlist("tags")
        if tag_ids:
            tags = Tag.objects.filter(id__in=tag_ids)
            image_instance.tags.set(tags)

        serializer = self.get_serializer(image_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        if "image" in request.data:
            return Response(
                {"error": "Image field cannot be updated"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial,
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
