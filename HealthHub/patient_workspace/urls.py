from django.urls import path
from . import views

app_name = 'patient_workspace'
urlpatterns = [
    path('', views.patient_dashboard, name='patient_dashboard'),
]