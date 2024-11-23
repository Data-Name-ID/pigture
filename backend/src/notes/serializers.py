import rest_framework.serializers

import notes.models


class NoteSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = notes.models.Note
        fields = (
            notes.models.Note.name.field.name,
            notes.models.Note.description.field.name,
            notes.models.Note.author.field.name,
        )
