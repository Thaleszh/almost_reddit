"""
Accounts URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include


###
# URL Patterns
###
urlpatterns = [
    url(r'^', include('comment.api.v1.urls'))
]
