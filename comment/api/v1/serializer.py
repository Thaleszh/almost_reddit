from rest_framework.serializers import ModelSerializer
from comment.models import Comment


class ReadCommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'title', 'author', 'post', 'created_at', 'updated_at', 'content']


class ChangeCommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'title', 'author', 'post', 'content']
