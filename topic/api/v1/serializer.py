from rest_framework.serializers import ModelSerializer
from topic.models import Topic
from user.api.v1.serializer import UserSerializer


class TopicSerializer(ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Topic
        fields = ['id', 'name', 'title', 'author', 'url_name', 'created_at', 'updated_at', 'description']
