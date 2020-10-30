from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from post.api.v1.serializer import ChangePostSerializer, ReadPostSerializer
from post.models import Post


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ChangePostSerializer

    def list(self, request, topic_pk=None,):
        queryset = Post.objects.filter(topic=topic_pk)
        serializer = ReadPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, topic_pk=None):
        queryset = Post.objects.filter(pk=pk, topic=topic_pk)
        post = get_object_or_404(queryset, pk=pk)
        serializer = ReadPostSerializer(post)
        return Response(serializer.data)