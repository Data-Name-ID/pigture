from django.contrib.auth.models import User
from django.db import models

import core.models
import marking.models


class Image(core.models.NameAbstractModel):
    image = models.ImageField(verbose_name="изображение", upload_to="images/")
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
    description = models.TextField(
        verbose_name="описание",
        default="",
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
