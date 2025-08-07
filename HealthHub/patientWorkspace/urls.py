from django.urls import path
from . import views

app_name = 'patientWorkspace'
urlpatterns = [
    path('', views.patient_dashboard, name='patient_dashboard'),

    path('diagnose_symptoms/', views.diagnose_symptoms, name='diagnose_symptoms'),
]