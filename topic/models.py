from django.db import models
from accounts.models import User


# Create your models here.
class Topic(models.Model):
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

    description = models.TextField()

    url_name = models.SlugField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
