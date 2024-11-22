from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from images.models import Image


class ImageUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        print("hello world")
        file_obj = request.data.get("image", None)
        if not file_obj:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        image_instance = Image.objects.create(image=file_obj)

        return Response(
            {
                "message": "Image uploaded successfully",
                "image_id": image_instance.id,
                "image_url": image_instance.image.url,
                "uploaded_at": image_instance.uploaded_at,
            },
            status=status.HTTP_201_CREATED,
        )
