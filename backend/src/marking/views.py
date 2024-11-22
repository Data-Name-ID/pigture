from rest_framework import viewsets

import marking.models
import marking.serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = marking.models.Category.objects.all()
    serializer_class = marking.serializers.CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = marking.models.Tag.objects.all()
    serializer_class = marking.serializers.TagSerializer


__all__ = [CategoryViewSet, TagViewSet]
