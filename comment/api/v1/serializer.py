from rest_framework.serializers import ModelSerializer
from comment.models import Comment


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'title', 'author', 'created_at', 'updated_at', 'post', 'content']
