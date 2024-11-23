from django.contrib.auth.models import User
from django.db import models

from images.models import Image


class Note(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notes",
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="notes",
    )
    name = models.CharField(
        verbose_name="название",
        db_column="name",
        help_text="Укажите название заметки",
        max_length=150,
    )
    description = models.TextField(
        verbose_name="описание",
        default="",
        blank=True,
    )

    class Meta:
        verbose_name = "заметка"
        verbose_name_plural = "заметки"

    def __str__(self):
        return f"Заметка пользователя {self.author.name}"
