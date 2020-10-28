from django.conf.urls import url, include
from rest_framework import routers

from comment.api.v1.views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet, basename='comment')

urlpatterns = [
    url(r'^', include(router.urls))
]
