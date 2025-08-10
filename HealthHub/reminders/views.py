from django.shortcuts import render, redirect
from .models import Reminder

# Create your views here.

def reminders_dash(request):
    return render(request, 'reminders/reminders_dash.html', {'reminders': Reminder.objects.filter(user=request.user).order_by('due_date')})

def add_reminder(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        due_date = request.POST.get('due_date')
        reminder = Reminder.objects.create(user=request.user, title=title, content=content, due_date=due_date)
        reminder.save()
        return redirect('reminders:reminders_dash')
    return render(request, 'reminders/add_reminder.html')

def complete_reminder(request, Reminder_id):
    Reminder.objects.get(id=Reminder_id).delete()
    return redirect('reminders:reminders_dash')

def update_reminder(request, Reminder_id):
    reminder = Reminder.objects.get(id=Reminder_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        due_date = request.POST.get('due_date')
        reminder.title = title
        reminder.content = content
        reminder.due_date = due_date
        reminder.save()
    return redirect('reminders:reminders_dash')