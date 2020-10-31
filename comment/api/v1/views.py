from rest_framework.viewsets import ModelViewSet

from accounts.api.v1.permissions import IsOwnerOrReadOnly
from comment.api.v1.serializer import CommentSerializer
from comment.models import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def filter_queryset(self, queryset):
        current_post_pk = self.kwargs.get('post_pk')
        return queryset.filter(post_id=current_post_pk)
