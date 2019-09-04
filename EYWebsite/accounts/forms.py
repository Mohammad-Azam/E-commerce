from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    username=forms.CharField(help_text='')
    password1=forms.CharField(widget=forms.PasswordInput,help_text='at least 8 characters and not entirely numeric')
    
    class Meta:
        model=User
        fields=['username','email','password1']
class LoginForm(forms.Form):
    first_name=forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)
    email=forms.EmailField()


