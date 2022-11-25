from django import forms
from django.forms import widgets

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']
        widgets = {
            'type': widgets.CheckboxSelectMultiple,
            'description': widgets.Textarea(attrs={'placeholder': 'Описание Задачи'})
        }