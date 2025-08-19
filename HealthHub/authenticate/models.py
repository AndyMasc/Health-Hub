from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('Doctor', 'Doctor'), ('Patient', 'Patient')], default='Patient')

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Account, on_delete=models.CASCADE, limit_choices_to={'role': 'Doctor'}, related_name='patients', null=True, blank=True)
