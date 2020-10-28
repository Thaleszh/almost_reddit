from rest_framework.viewsets import ModelViewSet

from comment.api.v1.serializer import CommentSerializer
from comment.models import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()

    serializer_class = CommentSerializer
