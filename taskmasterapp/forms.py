from django import forms
from django.forms import ModelForm, TextInput
from .models import Task 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority']
        widgets = {

                'title': TextInput(attrs={'style': 'color: blue'}),
                'due_date': forms.DateInput(attrs={'type': 'date'}),
                'priority': forms.Select(),

        }

        labels = {
            "title": "Título",
            "due_date": "Data",
            "priority": "Prioridade"
        }