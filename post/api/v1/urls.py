from django.conf.urls import url, include
from rest_framework_nested import routers

from post.api.v1.views import PostViewSet
from topic.api.v1.urls import router


post_router = routers.NestedSimpleRouter(router, r'topic', lookup='topic')
post_router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    url(r'^', include(post_router.urls))
]
