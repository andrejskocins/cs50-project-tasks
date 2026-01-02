from django import forms
from .models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Task title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Description (optional)"}),
            "due_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}, format="%Y-%m-%d"),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control", "rows": 2, "placeholder": "Add a comment"}),
        }
