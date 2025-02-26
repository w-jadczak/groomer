from django.test import TestCase
from rest_framework.test import APIClient

from users.models import User


class CustomTokenObtainPairViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", password="password123?", email="test@test.com", mobile="9876543210", is_active=True
        )
        self.client = APIClient()
        self.token_url = "/api/auth/token/"

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
