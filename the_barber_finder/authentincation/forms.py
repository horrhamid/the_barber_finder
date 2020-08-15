from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'email'
        )