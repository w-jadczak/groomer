from rest_framework import generics

from users.serializers import UserSerializer
from users.models import User


class UserListCreateView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
