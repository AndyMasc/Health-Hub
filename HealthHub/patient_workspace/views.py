from django.shortcuts import render

# Create your views here.

def patient_dashboard(request):
    return render(request, 'patient_workspace/patient_dash.html')