from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from accounts.api.v1.permissions import IsOwnerOrReadOnly
from comment.api.v1.serializer import CommentSerializer
from comment.models import Comment
from post.models import Post


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def filter_queryset(self, queryset):
        post_pk = self.kwargs.get('post_pk')
        return queryset.filter(post_id=post_pk)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, post_pk=self.kwargs.get('post_pk'))
        serializer.save(post=post)
