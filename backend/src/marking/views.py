from rest_framework import viewsets
from rest_framework import status, decorators
from rest_framework.response import Response

import marking.models
import marking.serializers
import images.serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = marking.models.Category.objects.all()
    serializer_class = marking.serializers.CategorySerializer

    @decorators.action(methods=["get"], detail=True)
    def images(self, request, pk=None):
        patient = self.get_object()
        images_set = patient.images.all()
        serializer = images.serializers.ImageSerializer(images_set, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = marking.models.Tag.objects.all()
    serializer_class = marking.serializers.TagSerializer
