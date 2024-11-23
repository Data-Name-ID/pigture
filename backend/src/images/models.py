from django.db import models

import marking.models
import patients.models
import core.models


class Image(core.models.AbstractNameModel):
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
    patient = models.ForeignKey(
        patients.models.Patient,
        on_delete=models.CASCADE,
        related_name="images",
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name="описание",
        null=True,
        blank=True,
    )
    metadata = models.JSONField(
        verbose_name="метаданные",
        default=dict,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "картинка"
        verbose_name_plural = "картинки"

    def __str__(self):
        return f"{self.image.name} - {self.uploaded_at}"
