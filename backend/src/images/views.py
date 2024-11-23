from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from images.models import Image, Tiles
from images.serializers import ImageSerializer
from images.tasks import process_image
from marking.models import Category, Tag


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

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
            author=request.user,
        )

        tag_ids = request.data.getlist("tags")
        if tag_ids:
            tags = Tag.objects.filter(id__in=tag_ids)
            image_instance.tags.set(tags)

        process_image(image_instance.image.path, image_instance.id)
        Tiles.objects.create(
            image=image_instance,
            file=f"tiles/{image_instance.id}/tiles.dzi",
        )

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
