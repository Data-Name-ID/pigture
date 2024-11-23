from django.contrib.auth.models import User
from django.db import models

import core.models
import marking.models
import patients.models
import core.models


class Note(core.models.AbstractNameModel):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="notes",
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name="описание",
        default="",
        blank=True,
    )
