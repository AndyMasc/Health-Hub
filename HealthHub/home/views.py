from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from authenticate.models import Account

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if request.user.account.role == 'Patient':
            return redirect('patient_workspace:dashboard')
        elif request.user.account.role == 'Doctor':
            return redirect('patient_workspace:dashboard')
    return render(request, 'home/index.html')