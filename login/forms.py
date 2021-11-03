from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from login.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
