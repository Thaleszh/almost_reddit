from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

import comment.api.v1.serializer as serializer
from comment.models import Comment


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializer.ReadCommentSerializer
        return serializer.ChangeCommentSerializer
