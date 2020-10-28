from rest_framework.viewsets import ModelViewSet

from user.api.v1.serializer import UserSerializer
from accounts.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer
