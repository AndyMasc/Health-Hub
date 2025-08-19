from django.urls import path
from . import views

app_name = 'authenticate'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('account/', views.account, name='account'),

    path('delete_account/', views.delete_account, name='delete_account'),
    path('update_user/', views.update_user, name='update_user'),

    path('add_patient/', views.add_patient, name='add_patient'),
]
