from django.shortcuts import render, redirect
from .models import Reminder
from django.utils import timezone

# Create your views here.

def reminders_dash(request):
    overdue_reminders = Reminder.objects.filter(
        user=request.user,
        is_completed=False,
        due_date__lt=timezone.now().date()
    )
    return render(request, 'reminders/reminders.html', {
        'reminders': Reminder.objects.filter(user=request.user, is_completed=False).order_by('due_date'),
        'completed_reminders': Reminder.objects.filter(user=request.user, is_completed=True).order_by('due_date').count(),
        'overdue_reminders': overdue_reminders,
        'reminders_due_today': Reminder.objects.filter(due_date=timezone.now().date())
    })

def add_reminder(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        due_date = request.POST.get('due_date')
        if not due_date:
            due_date = None
        reminder = Reminder.objects.create(user=request.user, title=title, content=content, due_date=due_date)
        reminder.save()
        return redirect('reminders:reminders_dash')
    return render(request, 'reminders/add_reminder.html')

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