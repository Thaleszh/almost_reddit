from rest_framework.viewsets import ModelViewSet

import post.api.v1.serializer as serializer
from post.models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializer.ReadPostSerializer
        return serializer.ChangePostSerializer
