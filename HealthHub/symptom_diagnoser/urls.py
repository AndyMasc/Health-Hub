from django.urls import path
from . import views

app_name = 'symptom_diagnoser'
urlpatterns = [
    path('', views.symptom_diagnoser, name='symptom_diagnoser'),
]