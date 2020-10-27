from django.db import models


# Create your models here.
class Comment(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(
        max_length=64
    )

    author = models.ForeignKey(
        to= 'accounts.User',
        on_delete=models.CASCADE
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    post = models.ForeignKey(
        to='post.Post',
        on_delete=models.CASCADE
    )
