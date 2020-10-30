from rest_framework.serializers import ModelSerializer
from topic.models import Topic


class ReadTopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'title', 'author', 'url_name', 'created_at', 'updated_at', 'description']


class ChangeTopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'title', 'author', 'url_name', 'description']
