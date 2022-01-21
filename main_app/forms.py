from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=25)
    city = forms.CharField(max_length=25)
    state = forms.CharField(max_length=2)
    zip = forms.IntegerField()

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name", "phone_number", "address", "city", "state", "zip"]