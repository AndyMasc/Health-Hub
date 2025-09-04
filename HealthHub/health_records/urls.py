from django.urls import path
from . import views

app_name = 'health_records'
urlpatterns = [
    path('<int:patient_id>/', views.health_records, name='health_records'),
    path('add_record/', views.add_record, name='add_record'),
    path('record_history/<int:patient_id>/', views.record_history, name='record_history'),
]
