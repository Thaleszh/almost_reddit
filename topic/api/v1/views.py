from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from topic.api.v1.serializer import ReadTopicSerializer, ChangeTopicSerializer
from topic.models import Topic


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = ChangeTopicSerializer

    def list(self, request,):
        queryset = Topic.objects.filter()
        serializer = ReadTopicSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Topic.objects.filter()
        topic = get_object_or_404(queryset, pk=pk)
        serializer = ReadTopicSerializer(topic)
        return Response(serializer.data)