from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CreateUserForm, AuthorizeUser, UpdateUser, AddPatientForm
from .models import Patient, Account


# Create your views here.

@login_required
def account(request):
    form = UpdateUser(instance=request.user)
    context = {'form': form}
    return render(request, 'authenticate/account.html', context)


def update_user(request):
    if request.method == 'POST':
        form = UpdateUser(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully')
            return redirect('authenticate:account')
        else:
            # Display form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = UpdateUser(instance=request.user)
    return render(request, 'authenticate/account.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
    else:
        form = CreateUserForm()
        context = {'form': form}
    return render(request, 'authenticate/register.html', context)


def signin(request):
    form = AuthorizeUser()
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'authenticate/signin.html', context)


@login_required()
def signout(request):
    logout(request)
    return redirect('home:index')


@login_required()
def delete_account(request):
    user = request.user
    user.delete()
    messages.success(request, 'Your account has been deleted successfully.')
    return redirect('authenticate:signin')


@login_required()
def add_patient(request):
    form = AddPatientForm()
    context = {'form': form}
    if request.method == 'POST':
        patient_user = request.POST.get('patient_user')
        patient_password = request.POST.get('patient_password')
        patient_obj = authenticate(username=patient_user, password=patient_password)

        if patient_obj is not None:
            patient = Account.objects.get(user=patient_obj)
            doctor = Account.objects.get(user=request.user)
            patient.doctor = doctor
            patient.save()
            return redirect('workspace:dashboard')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'authenticate/add_patient.html', {'form': form})