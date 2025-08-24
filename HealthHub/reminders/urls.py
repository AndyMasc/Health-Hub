from django.urls import path
from . import views

app_name = 'reminders'
urlpatterns = [
    path('', views.reminders_dash, name='reminders_dash'),
    path('add_reminder/', views.add_reminder, name='add_reminder'),
    path('complete_reminder/<int:Reminder_id>/', views.complete_reminder, name='complete_reminder'),
    path('update_reminder/<int:Reminder_id>', views.update_reminder, name='update_reminder'),
    path('delete_reminder/<int:Reminder_id>', views.delete_reminder, name='delete_reminder'),
]