from django.db import models

from users.models import User


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    species = models.CharField(max_length=100, default="dog")
    breed = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
