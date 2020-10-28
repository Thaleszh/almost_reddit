from django.conf.urls import url, include
from rest_framework import routers

from topic.api.v1.views import TopicViewSet

router = routers.DefaultRouter()
router.register(r'topic', TopicViewSet, basename='topic')

urlpatterns = [
    url(r'^', include(router.urls))
]
