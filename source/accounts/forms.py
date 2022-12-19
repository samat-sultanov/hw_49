from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class MyUserCreationForm(UserCreationForm):
    email = forms.CharField(max_length=30, required=True, label='Email')

    def clean(self):
        if self.cleaned_data["first_name"].strip() == '' and self.cleaned_data["last_name"].strip() == '':
            raise ValidationError("Одно из полей (first_name, last_name) должно быть заполнено")

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
