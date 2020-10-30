from rest_framework.viewsets import ModelViewSet

import comment.api.v1.serializer as serializer
from comment.models import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializer.ReadCommentSerializer
        return serializer.ChangeCommentSerializer
