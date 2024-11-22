from django.db import models


class AbstractModel(models.Model):
    name = models.CharField(
        verbose_name="название",
        db_column="name",
        help_text="Укажите название",
        max_length=150,
        unique=True,
    )

    def __str__(self):
        return self.name
