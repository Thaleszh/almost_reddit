from rest_framework.viewsets import ModelViewSet

from accounts.api.v1.permissions import IsOwnerOrReadOnly
from post.api.v1.serializer import PostSerializer
from post.models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def filter_queryset(self, queryset):
        topic_url_name = self.kwargs.get('topic_url_name')
        return queryset.filter(topic__url_name=topic_url_name)

