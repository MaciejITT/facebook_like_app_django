from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    sexes = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Neither', 'Neither')
    )
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=200, required=True, help_text='Required. Enter valid email address')
    sex = forms.ChoiceField(choices=sexes, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'sex', 'email', 'password1', 'password2',)


class UpdateUserInfo(UserChangeForm):
    sexes = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Neither', 'Neither')
    )
    sex = forms.ChoiceField(choices=sexes, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'sex', 'email')
        exclude = ('password',)
