from django.db import models

from pets.models import Pet
from services.models import Service
from users.models import User


class Appointment(models.Model):
    client = models.ForeignKey(User, related_name="client_appointments", on_delete=models.CASCADE)
    worker = models.ForeignKey(
        User, related_name="worker_appointments", on_delete=models.SET_NULL, null=True, blank=True
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AppointmentService(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
