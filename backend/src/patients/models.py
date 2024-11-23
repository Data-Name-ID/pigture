from django.db import models


class Patient(models.Model):
    uuid = models.UUIDField()

    class Meta:
        verbose_name = "пациент"
        verbose_name_plural = "пациенты"

    def __str__(self):
        return f"Пациент с id {self.uuid}"
