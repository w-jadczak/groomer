from rest_framework import serializers

from pets.models import Pet


class PerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "owner", "name", "species", "breed", "age", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
