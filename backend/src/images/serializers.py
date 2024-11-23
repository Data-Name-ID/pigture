from rest_framework import serializers

from images.models import Image, Tiles


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "id",
            "image",
            "uploaded_at",
            "category",
            "tags",
            "name",
            "description",
            "metadata",
        ]
        read_only_fields = ["uploaded_at"]


class TilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiles
        fields = [
            "id",
            "image_id",
            "file",
        ]
