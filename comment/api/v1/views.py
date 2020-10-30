from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accounts.api.v1.permissions import IsOwnerOrReadOnly
from comment.api.v1.serializer import ReadCommentSerializer, ChangeCommentSerializer
from comment.models import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ChangeCommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request, topic_pk=None, post_pk=None):
        queryset = Comment.objects.filter(post=post_pk)
        serializer = ReadCommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, topic_pk=None, post_pk=None):
        queryset = Comment.objects.filter(pk=pk, post=post_pk)
        comment = get_object_or_404(queryset, pk=pk)
        serializer = ReadCommentSerializer(comment)
        return Response(serializer.data)