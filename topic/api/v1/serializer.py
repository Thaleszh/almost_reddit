from rest_framework.serializers import ModelSerializer
from topic.models import Topic


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'title', 'author', 'created_at', 'updated_at', 'url_name', 'description']
