from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accounts.api.v1.permissions import IsOwnerOrReadOnly
from post.api.v1.serializer import ChangePostSerializer, ReadPostSerializer
from post.models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ChangePostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request, topic_pk=None,):
        queryset = Post.objects.filter(topic=topic_pk)
        serializer = ReadPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, topic_pk=None):
        queryset = Post.objects.filter(pk=pk, topic=topic_pk)
        post = get_object_or_404(queryset, pk=pk)
        serializer = ReadPostSerializer(post)
        return Response(serializer.data)