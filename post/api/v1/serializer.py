from rest_framework.serializers import ModelSerializer
from post.models import Post
from topic.api.v1.serializer import TopicSerializer
from user.api.v1.serializer import UserSerializer


class PostSerializer(ModelSerializer):
    # topic = TopicSerializer()
    # author = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'topic', 'created_at', 'updated_at', 'content']
