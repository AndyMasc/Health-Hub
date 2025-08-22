from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Reminder(models.Model):
    user = models.ManyToManyField(User, related_name='reminders')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title