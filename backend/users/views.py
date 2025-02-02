from rest_framework import viewsets

from pets.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer