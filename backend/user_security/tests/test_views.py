from django.test import TestCase
from users.models import User


class CustomTokenObtainPairViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", password="password123?", email="test@test.com", mobile="9876543210", is_active=True
        )
        self.token_url = "/api/auth/login/"

    def test_should_return_token(self):
        response = self.client.post(self.token_url, {"username": "test", "password": "password123?"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_should_return_no_active_user_found(self):
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.token_url, {"username": "test", "password": "password123?"}, format="json")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data["detail"], "No active account found with the given credentials")

    def test_should_return_invalid_credentials(self):
        response = self.client.post(
            self.token_url, {"username": "non_existing_user", "password": "bad_password"}, format="json"
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data["detail"], "No active account found with the given credentials")


class RegisterViewTest(TestCase):
    def setUp(self):
        self.register_url = "/api/auth/register/"
        self.data = {
            "username": "newuser",
            "email": "newuser@test.com",
            "mobile": 987654321,
            "password": "password123!",
            "password2": "password123!",
            "first_name": "John",
            "last_name": "Doe",
        }

    def test_should_create_user(self):
        response = self.client.post(self.register_url, self.data, format="json")
        users = User.objects.all()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(users.count(), 1)
        user = users.first()
        self.assertEqual(user.username, self.data["username"])
        self.assertEqual(user.email, self.data["email"])
        self.assertEqual(user.first_name, self.data["first_name"])
        self.assertEqual(user.last_name, self.data["last_name"])
        self.assertTrue(user.check_password(self.data["password"]))

    def test_should_return_created(self):
        response = self.client.post(self.register_url, self.data, format="json")
        self.assertEqual(response.status_code, 201)


class LogoutViewTest(TestCase):
    def setUp(self):
        self.logout_url = "/api/auth/logout/"
        self.user = User.objects.create_user(
            username="test", password="password123?", email="test@test.com", mobile="9876543210", is_active=True
        )
        response = self.client.post("/api/auth/login/", {"username": "test", "password": "password123?"})
        self.access_token = response.data["access"]
        self.refresh_token = response.data["refresh"]

    def test_should_logout(self):
        response = self.client.post(
            self.logout_url, HTTP_REFRESH_TOKEN=self.refresh_token, HTTP_AUTHORIZATION="Bearer " + self.access_token
        )
        self.assertEqual(response.status_code, 205)
        self.assertEqual(response.data["detail"], "Logged out successfully")

    def test_should_not_logout_without_refresh_token(self):
        response = self.client.post(
            self.logout_url, HTTP_REFRESH_TOKEN=None, HTTP_AUTHORIZATION="Bearer " + self.access_token
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["detail"], "No refresh token provided")

    def test_should_not_logout_with_invalid_refresh_token(self):
        invalid_refresh_token = "invalid_token"
        response = self.client.post(
            self.logout_url, HTTP_REFRESH_TOKEN=invalid_refresh_token, HTTP_AUTHORIZATION="Bearer " + self.access_token
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.data["detail"], "Token is invalid or expired")
