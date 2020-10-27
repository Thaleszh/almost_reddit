from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(
        max_length=64
    )

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    topic = models.ForeignKey(
        to='topic.Topic',
        on_delete=models.CASCADE
    )
