from pyexpat import model
from django import forms
from django.contrib.auth.models import User

class Login_form(forms.ModelForm):

    username = forms.CharField(label='user')
    password = forms.CharField(label='pass',widget=forms.PasswordInput())    
    class Meta:
        model = User
        fields = ['username', 'password']
