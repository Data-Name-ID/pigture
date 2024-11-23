import rest_framework.serializers

import marking.models


class CategorySerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = marking.models.Category
        fields = (
            marking.models.Category.id.field.name,
            marking.models.Category.name.field.name,
        )


class TagSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = marking.models.Tag
        fields = (
            marking.models.Tag.id.field.name,
            marking.models.Tag.name.field.name,
        )
