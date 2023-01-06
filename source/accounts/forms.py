from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from accounts.models import Profile


class MyUserCreationForm(UserCreationForm):
    email = forms.CharField(max_length=30, required=True, label='Email')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['first_name'].strip() == '' and cleaned_data['last_name'].strip() == '':
            raise ValidationError('Одно из полей (first_name, last_name) должно быть заполнено!')
        return cleaned_data

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['url_github', 'avatar', 'about']