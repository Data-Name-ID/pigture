import rest_framework.serializers

import marking.models


class CategorySerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = marking.models.Category
        fields = "__all__"


class TagSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = marking.models.Tag
        fields = "__all__"
