from django.test import TestCase

from user_security.serializers import CustomTokenObtainPairSerializer, RegisterSerializer
from users.models import User


class CustomTokenObtainPairSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", email="test@test.com", mobile="9876543210")

    def tearDown(self):
        self.user.delete()

    def test_token_should_contain_username(self):
        token = CustomTokenObtainPairSerializer.get_token(self.user)

        self.assertIn("username", token)
        self.assertEqual(token["username"], self.user.username)


class RegisterSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", email="test@test.com", mobile="9876543210")
        self.data = {
            "username": "newuser",
            "email": "newuser@test.com",
            "mobile": 987654321,
            "password": "password123!",
            "password2": "password123!",
            "first_name": "John",
            "last_name": "Doe",
        }

    def tearDown(self):
        self.user.delete()

    def test_should_throw_error_when_passwords_differ(self):
        data = self.data.copy()
        data["password2"] = "<PASSWORD>!"
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password2", serializer.errors)
        self.assertEqual(serializer.errors["password2"][0], "Passwords do not match")

    def test_should_throw_error_when_password_is_empty(self):
        data = self.data.copy()
        data["password"] = ""
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
        self.assertEqual(serializer.errors["password"][0], "This field may not be blank.")

    def test_should_throw_error_when_mobile_exists(self):
        data = self.data.copy()
        data["mobile"] = self.user.mobile
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("mobile", serializer.errors)
        self.assertEqual(serializer.errors["mobile"][0], "This field must be unique.")

    def test_should_throw_error_when_email_exists(self):
        data = self.data.copy()
        data["email"] = self.user.email
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        self.assertEqual(serializer.errors["email"][0], "This field must be unique.")

    def test_should_create_new_user(self):
        serializer = RegisterSerializer(data=self.data)

        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, self.data["username"])
        self.assertEqual(user.email, self.data["email"])
        self.assertEqual(user.mobile, self.data["mobile"])
