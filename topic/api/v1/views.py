from rest_framework.viewsets import ModelViewSet

import topic.api.v1.serializer as serializer
from topic.models import Topic


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializer.ReadTopicSerializer
        return serializer.ChangeTopicSerializer
