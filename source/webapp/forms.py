from django import forms
from django.core.exceptions import ValidationError
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

    def clean(self):
        sql_keywords = ['select', 'delete', 'insert', 'update', 'create']
        summary = self.cleaned_data.get('summary')
        description = self.cleaned_data.get('description')
        if description:
            if len(summary) > len(description):
                raise ValidationError('Описание задачи не может быть меньше заголовка!')