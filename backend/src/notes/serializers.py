import rest_framework.serializers

import notes.models


class NoteSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = notes.models.Note
        fields = "__all__"
