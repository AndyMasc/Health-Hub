from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import HealthRecord
from authenticate.models import Doctor, Patient, Account

# Create your views here.

def health_records(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient_user = User.objects.get(patient=patient)
    if (patient.doctor.user == request.user) or (patient_user == User.objects.get(id=patient_id)):
        return render(request, 'health_records/health_records.html', {
            'record': HealthRecord.objects.filter(viewers=patient_user).order_by('-record_creation_date').first(),
            'patient': patient_user,
        })
    else:
        raise Http404('You\'re not allowed here')

def add_record(request):
    if request.user.account.role == 'Doctor':
        if request.method == 'POST':
            address = request.POST.get('address')
            language = request.POST.get('language')
            weight = request.POST.get('weight')
            height = request.POST.get('height')
            allergies = request.POST.get('allergies')
            medication_history = request.POST.get('medication_history')
            extra_notes = request.POST.get('extra_notes')
            current_doctor = request.POST.get('current_doctor')
            share_recipient = request.POST.get('share_recipient')
            share_recipient = User.objects.get(username=share_recipient)

            record = HealthRecord.objects.create(address=address, language=language, weight=weight, height=height, allergies=allergies, medication_history=medication_history, extra_notes=extra_notes, current_doctor=current_doctor)
            doctor = request.user
            patient = share_recipient
            record.viewers.add(patient, doctor)
            record.save()
            return redirect('workspace:dashboard')
        return render(request, 'health_records/add_record.html', {'patients':request.user.doctor.patients.all()})
    else:
        raise Http404('You\'re not allowed to see this page.')

