from rest_framework.serializers import ModelSerializer
from comment.models import Comment
from post.api.v1.serializer import PostSerializer
from user.api.v1.serializer import UserSerializer


class CommentSerializer(ModelSerializer):
    # author = UserSerializer()
    # post = PostSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'title', 'author', 'post', 'created_at', 'updated_at', 'content']
