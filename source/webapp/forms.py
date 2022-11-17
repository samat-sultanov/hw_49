from django import forms
from django.forms import widgets

from webapp.models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=100, required=True, label='Заголовок')
    description = forms.CharField(max_length=1000, required=False, label='Описание',
                                  widget=widgets.Textarea(attrs={'cols': 40, 'rows': 3}))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Тип')
