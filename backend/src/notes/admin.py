import django.contrib

import notes.models


@django.contrib.admin.register(notes.models.Note)
class NotesAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        notes.models.Note.name.field.name,
        notes.models.Note.description.field.name,
    )
