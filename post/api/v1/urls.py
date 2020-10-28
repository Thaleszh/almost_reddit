from django.conf.urls import url, include
from rest_framework import routers

from post.api.v1.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    url(r'^', include(router.urls))
]
