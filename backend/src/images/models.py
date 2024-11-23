from django.conf import settings
from django.db import models

import marking.models


class Image(models.Model):
    image = models.ImageField(verbose_name="изображение", upload_to="images/")
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
    name = models.CharField(
        max_length=255,
        verbose_name="название",
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name="описание",
        null=True,
        blank=True,
    )
    metadata = models.JSONField(
        verbose_name="мета данные",
        default=dict,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "картинка"
        verbose_name_plural = "картинки"

    def __str__(self):
        return f"{self.image.name} - {self.uploaded_at}"


class Tiles(models.Model):
    def _upload_to(self, filename):
        return f"tiles/{self.image_id}/{filename}"

    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    file = models.FileField(upload_to=_upload_to)