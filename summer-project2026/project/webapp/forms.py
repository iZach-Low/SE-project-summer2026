from django import forms

from .models import Note


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