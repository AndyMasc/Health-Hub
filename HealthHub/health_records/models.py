from django.contrib.auth.models import User
from django.db import models
from authenticate.models import Patient, Doctor


# Create your models here.

class HealthRecord(models.Model):
    viewers = models.ManyToManyField(User, related_name='viewers')

    address = models.CharField(max_length=300)
    language = models.CharField(max_length=100)

    weight = models.IntegerField()
    height = models.IntegerField()

    allergies = models.CharField(max_length=100)
    medication_history = models.CharField(max_length=300)

    extra_notes = models.TextField()

    current_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)

    record_creation_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

