from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateField(default=date.today)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )