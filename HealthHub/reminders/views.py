from django.shortcuts import render, redirect
from .models import Reminder

# Create your views here.

def reminders_dash(request):
    return render(request, 'reminders/reminders_dash.html', {'reminders': Reminder.objects.filter(user=request.user)})

def add_reminder(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        reminder = Reminder.objects.create(user=request.user, title=title, content=content)
        reminder.save()
        return redirect('reminders:reminders_dash')
    return render(request, 'reminders/add_reminder.html')