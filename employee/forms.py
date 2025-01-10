from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['employee', 'title', 'description', 'due_date', 'status']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # For datetime input
        }
