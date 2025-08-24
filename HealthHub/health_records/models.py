from django.contrib.auth.models import User
from django.db import models
from authenticate.models import Patient


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

    current_doctor = models.CharField(max_length=100)

    record_creation_date = models.DateField(auto_now_add=True, null=True, blank=True)

