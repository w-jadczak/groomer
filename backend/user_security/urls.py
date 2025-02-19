from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user_security.views import RegisterView, CustomTokenObtainPairView

app_name = "user_security"

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("register", RegisterView.as_view(), name="register"),
]
