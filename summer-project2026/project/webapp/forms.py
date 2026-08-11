from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Assignment, Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "class_name", "content"]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Note title",
                }
            ),
            "class_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Class name",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 12,
                    "placeholder": "Type your notes here...",
                }
            ),
        }


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