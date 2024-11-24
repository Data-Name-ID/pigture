from rest_framework import serializers

from images.models import Image, Tiles


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
        read_only_fields = ["uploaded_at"]

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)


class TilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiles
        fields = "__all__"
