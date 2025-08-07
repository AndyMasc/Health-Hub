from django.shortcuts import render

# Create your views here.

def patient_dashboard(request):
    return render(request, 'patientWorkspace/patient_dash.html')

def diagnose_symptoms(request):

    return render(request, 'patientWorkspace/diagnose_symptoms.html')