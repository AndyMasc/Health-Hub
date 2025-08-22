from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Reminder
from django.utils import timezone
from authenticate.models import Account, Patient

# Create your views here.

def reminders_dash(request):
    now = timezone.now()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    high_priority_reminders = Reminder.objects.filter(user=request.user, is_completed=False, due_date__lt=today_start)
    return render(request, 'reminders/reminders.html', {
        'reminders': Reminder.objects.filter(user=request.user, is_completed=False).order_by('due_date'),
        'completed_reminders': Reminder.objects.filter(user=request.user, is_completed=True).order_by('due_date').count(),
        'high_priority_reminders': high_priority_reminders,
    })

def add_reminder(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        due_date = request.POST.get('due_date')
        share_recipient = request.POST.get('share_recipient')
        if not due_date:
            due_date = None
        reminder = Reminder.objects.create(title=title, content=content, due_date=due_date, created_by=request.user)
        if share_recipient:
            patient_user = User.objects.get(username=share_recipient)
            reminder.user.add(request.user, patient_user)
        else:
            reminder.user.add(request.user)
        reminder.save()
        return redirect('reminders:reminders_dash')
    if request.user.account.role == 'Doctor':
        patients = request.user.doctor.patients.all()
        return render(request, 'reminders/add_reminder.html', {'patients': patients})
    else:
        doctor = request.user.patient.doctor
        return render(request, 'reminders/add_reminder.html', {'doctor': doctor})

def complete_reminder(request, Reminder_id):
    reminder = Reminder.objects.get(id=Reminder_id)
    reminder.is_completed = True
    reminder.save()
    return redirect('reminders:reminders_dash')

def update_reminder(request, Reminder_id):
    reminder = Reminder.objects.get(id=Reminder_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        due_date = request.POST.get('due_date')
        if not due_date:
            due_date = None
        reminder.due_date = due_date
        reminder.title = title
        reminder.content = content
        reminder.save()
    return redirect('reminders:reminders_dash')

def delete_reminder(request, Reminder_id):
    reminder = Reminder.objects.get(id=Reminder_id)
    reminder.delete()
    return redirect('reminders:reminders_dash')