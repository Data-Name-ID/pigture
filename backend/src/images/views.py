from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import core.permissions
from images.models import Image, Tiles
from images.serializers import ImageSerializer, TilesSerializer
from images.tasks import process_image


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all().order_by("-uploaded_at")
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [core.permissions.HasGroupPermission]
    required_groups = {
        "GET": ["main_docs", "docs"],
        "POST": ["main_docs", "docs", "labs"],
    }

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request},
        )
        serializer.is_valid(raise_exception=True)

        image_instance = serializer.save()

        process_image.delay(image_instance.file.path, image_instance.id)
        Tiles.objects.create(
            image=image_instance,
            file=f"tiles/{image_instance.id}/tiles.dzi",
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TilesViewSet(ModelViewSet):
    queryset = Tiles.objects.all()
    serializer_class = TilesSerializer

    http_method_names = ["get"]
