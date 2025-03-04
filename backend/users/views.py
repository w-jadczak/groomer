from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserSerializer
from users.models import User


class UserListCreateView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer
