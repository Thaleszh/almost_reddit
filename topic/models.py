from django.db import models
from accounts.models import User
from helpers.models import TimestampModel


class Topic(TimestampModel):
    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=64
    )

    title = models.CharField(
        max_length=64
    )

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    url_name = models.SlugField()

    description = models.TextField()

