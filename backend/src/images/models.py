from django.contrib.auth.models import User
from django.db import models

import core.models
import marking.models
import patients.models


def _upload_tile(self, filename):
    return f"tiles/{self.image_id}/{filename}"


class Image(core.models.AbstractNameModel):
    file = models.FileField(verbose_name="изображение", upload_to="images/")
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="images",
        null=True,
        blank=True,
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        marking.models.Category,
        help_text="Выберите категорию",
        on_delete=models.SET_NULL,
        related_name="images",
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(
        marking.models.Tag,
        blank=True,
        help_text="Выберите теги",
    )
    patient = models.ForeignKey(
        patients.models.Patient,
        on_delete=models.CASCADE,
        related_name="images",
        null=True,
        blank=True,
    )
    description = models.TextField(  # noqa: DJ001
        verbose_name="описание",
        default="",
        blank=True,
        null=True,
    )
    metadata = models.JSONField(
        verbose_name="метаданные",
        default=dict,
        null=True,
        blank=True,
    )
    tiles = models.FileField(null=True, blank=True, upload_to=_upload_tile)
    thumbnail = models.ImageField(
        upload_to="thumbnails/",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "картинка"
        verbose_name_plural = "картинки"

    def __str__(self):
        return f"{self.image.name} - {self.uploaded_at}"
