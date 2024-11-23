from django.db import models


class Patient(models.Model):
    uuid = models.UUIDField()

    def __str__(self):
        return f"Пациент с id {self.uuid}"
