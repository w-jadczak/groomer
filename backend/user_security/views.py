from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from groomer import settings
from user_security.serializers import CustomTokenObtainPairSerializer, RegisterSerializer
from users.models import User


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data.get("access")
        refresh_token = response.data.get("refresh")

        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=settings.SECURE_COOKIES,
            samesite="Strict",
            max_age=60 * 60 * 24 * 7,
        )

        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=settings.SECURE_COOKIES,
            samesite="Strict",
            max_age=60 * 15,
        )

        return response


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "message": "User was succesfully created",
            },
            status=status.HTTP_201_CREATED,
        )


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.COOKIES.get("refresh_token")
            if not refresh_token:
                return Response({"detail": "No refresh token provided"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            response = Response({"detail": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
            response.delete_cookie("access_token")
            response.delete_cookie("refresh_token")

            return response
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
