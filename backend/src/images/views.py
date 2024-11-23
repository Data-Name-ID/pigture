from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from images.models import Image
from marking.models import Category, Tag


class ImageUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        image = request.FILES.get("image")

        if not image:
            return Response(
                {"error": "No image provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        category = None
        category_id = request.data.get("category")

        if not Category.objects.filter(id=category_id).exists():
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        image_instance = Image.objects.create(image=image, category=category)

        tag_ids = request.data.getlist("tags")
        if tag_ids:
            tags = Tag.objects.filter(id__in=tag_ids)
            image_instance.tags.set(tags)

        return Response(
            {"message": "Success"},
            status=status.HTTP_200_OK,
        )
