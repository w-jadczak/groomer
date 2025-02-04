from rest_framework import serializers
from appointments.models import Appointment, AppointmentService


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["id", "created_at", "updated_at", "client", "worker", "pet", "date", "duration", "status"]
        read_only_fields = ["id", "created_at", "updated_at"]


class AppointmentServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentService
        fields = ["appointment", "service", "created_at"]
        read_only_fields = "created_at"
