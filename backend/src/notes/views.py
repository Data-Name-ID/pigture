from rest_framework import viewsets

import core.permissions
import notes.models
import notes.serializers


class NotesViewSet(viewsets.ModelViewSet):
    queryset = notes.models.Note.objects.all()
    serializer_class = notes.serializers.NoteSerializer
    permission_classes = [core.permissions.HasGroupPermission]
    required_groups = {
        "GET": ["main_docs", "docs"],
        "POST": ["main_docs", "docs"],
        "PUT": ["main_docs", "docs"],
        "PATCH": ["main_docs", "docs"],
    }
