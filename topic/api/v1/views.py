from rest_framework.viewsets import ModelViewSet

from accounts.api.v1.permissions import IsOwnerOrReadOnly
from topic.api.v1.serializer import TopicSerializer
from topic.models import Topic


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'url_name'
