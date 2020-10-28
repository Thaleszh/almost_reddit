from rest_framework.viewsets import ModelViewSet

from post.api.v1.serializer import PostSerializer
from post.models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    serializer_class = PostSerializer
