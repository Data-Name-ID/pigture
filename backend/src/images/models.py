from django.db import models

import core.models


class Category(core.models.AbstractModel):
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Tag(core.models.AbstractModel):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


class Image(models.Model):
    image = models.ImageField(verbose_name="картинка", upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        db_column="category_id",
        help_text="Выберите категорию",
        on_delete=models.SET_NULL,
        related_name="images",
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        help_text="Выберите теги",
    )

    class Meta:
        verbose_name = "картинка"
        verbose_name_plural = "картинки"

    def __str__(self):
        return f"{self.image.name} - {self.uploaded_at}"
