from rest_framework.serializers import ModelSerializer
from post.models import Post


class ReadPostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'topic', 'created_at', 'updated_at', 'content']


class ChangePostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'topic', 'content']
