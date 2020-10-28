from rest_framework.viewsets import ModelViewSet

from topic.api.v1.serializer import TopicSerializer
from topic.models import Topic


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()

    serializer_class = TopicSerializer
