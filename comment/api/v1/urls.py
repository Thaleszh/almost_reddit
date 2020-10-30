from django.conf.urls import url, include
from rest_framework_nested import routers

from comment.api.v1.views import CommentViewSet
from post.api.v1.urls import post_router


comment_router = routers.NestedSimpleRouter(post_router, r'post', lookup='post')
comment_router.register(r'comment', CommentViewSet, basename='comment')

urlpatterns = [
    url(r'^', include(comment_router.urls))
]
