from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Account


class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username - required for sign in'}),
                               max_length=30)
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email address'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
    role = forms.ChoiceField(
        label='Role - This cannot be changed later.',
        required=True,
        choices=[('Doctor', 'Doctor'), ('Patient', 'Patient')],
        initial='Patient',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            # Create the Account instance with the selected role
            Account.objects.create(
                user=user,
                role=self.cleaned_data['role']
            )
        return user


class AuthorizeUser(AuthenticationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username - case sensitive'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UpdateUser(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=30)
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email address'}))

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise ValidationError("A user with this username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("A user with this email already exists.")
        return email


class AddPatientForm(forms.Form):
    patient_user = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Patient username'}),
                                   max_length=30)
    patient_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Patient password'}))

    def clean_patient_user(self):
        patient_user = self.cleaned_data['patient_user']
        return patient_user

    def clean_patient_password(self):
        patient_password = self.cleaned_data['patient_password']
        return patient_password
