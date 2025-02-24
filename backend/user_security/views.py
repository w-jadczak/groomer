from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from user_security.serializers import CustomTokenObtainPairSerializer, RegisterSerializer
from users.models import User


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        from rest_framework import status

        return Response(
            {
                "user": serializer.data,
                "refresh": str(refresh),
                "access": str(refresh.token),
                "message": "User was succesfully created",
            },
            status=status.HTTP_201_CREATED,
        )
