from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('Doctor', 'Doctor'), ('Patient', 'Patient')], default='Patient')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male')
    full_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor = models.ManyToManyField(Doctor, related_name='patients', null=True, blank=True)

    def __str__(self):
        return self.user.username