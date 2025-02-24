from unittest import TestCase

from user_security.serializers import CustomTokenObtainPairSerializer
from users.models import User


class CustomTokenObtainPairSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", email="test@test.com", mobile="987654321")

    def test_token_should_contain_username(self):
        token = CustomTokenObtainPairSerializer.get_token(self.user)

        self.assertIn("username", token)
        self.assertEqual(token["username"], self.user.username)
