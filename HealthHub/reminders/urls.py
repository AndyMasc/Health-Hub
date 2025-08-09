from django.urls import path
from . import views

app_name = 'reminders'
urlpatterns = [
    path('', views.reminders_dash, name='reminders_dash'),
    path('add_reminder', views.add_reminder, name='add_reminder'),
]