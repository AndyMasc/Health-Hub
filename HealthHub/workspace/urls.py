from django.urls import path
from . import views

app_name = 'workspace'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('patients_view/', views.patients_view, name='patients_view'),
]