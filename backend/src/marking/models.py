import core.models


class Category(core.models.AbstractModel):
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Tag(core.models.AbstractModel):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"
