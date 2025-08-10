from django.urls import path
from . import views

app_name = 'patient_workspace'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]