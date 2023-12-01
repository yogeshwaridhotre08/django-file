# tasks/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Task
from django.contrib.auth.models  import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'completed']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
