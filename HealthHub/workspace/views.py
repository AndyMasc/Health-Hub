from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from authenticate.models import Account, Patient, Doctor

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'workspace/dashboard.html')

@login_required
def patients_view(request):
    if request.user.account.role == 'Doctor':
        doctor_account = Doctor.objects.get(user=request.user)
        patients = doctor_account.patients.all()

        context = {'patients':patients}
        return render(request, 'workspace/patients.html', context)
    else:
        raise Http404("You're not allowed here.")