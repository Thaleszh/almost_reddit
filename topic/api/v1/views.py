from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accounts.api.v1.permissions import IsOwnerOrReadOnly
from topic.api.v1.serializer import ReadTopicSerializer, ChangeTopicSerializer
from topic.models import Topic


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = ChangeTopicSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request,):
        queryset = Topic.objects.filter()
        serializer = ReadTopicSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Topic.objects.filter()
        topic = get_object_or_404(queryset, pk=pk)
        serializer = ReadTopicSerializer(topic)
        return Response(serializer.data)