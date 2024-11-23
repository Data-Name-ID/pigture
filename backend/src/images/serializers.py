from rest_framework import serializers
from images.models import Image

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
