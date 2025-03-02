from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user_security.views import RegisterView, LoginView, LogoutView

app_name = "user_security"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
