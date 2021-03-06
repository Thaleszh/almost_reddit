from django.db import models
from accounts.models import User
from helpers.models import TimestampModel


class Post(TimestampModel):
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

    topic = models.ForeignKey(
        to='topic.Topic',
        on_delete=models.CASCADE
    )
