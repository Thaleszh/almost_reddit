from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

import topic.api.v1.serializer as serializer
from topic.models import Topic


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializer.ReadTopicSerializer
        return serializer.ChangeTopicSerializer
