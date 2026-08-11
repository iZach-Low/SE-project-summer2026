from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Assignment


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = [
            "title",
            "class_name",
            "due_date",
        ]

        widgets = {
            "due_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            )
        }