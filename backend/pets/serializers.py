from rest_framework import serializers

from pets.models import Pet
from users.serializers import UserSerializer

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "owner", "name", "species", "breed", "age", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_owner(self, value):
        if not value.is_active:
            raise serializers.ValidationError("Owner must be an active user.")
        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")
        if len(value) > 100:
            raise serializers.ValidationError("Name is too long")
        return value

    def validate_species(self, value):
        if len(value) > 100:
            raise serializers.ValidationError("Species is too long")
        return value

    def validate_breed(self, value):
        if not value.strip():
            raise serializers.ValidationError("Breed cannot be empty")
        if len(value) > 100:
            raise serializers.ValidationError("Breed is too long")
        return value
    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age must be a positive number.")
        return value