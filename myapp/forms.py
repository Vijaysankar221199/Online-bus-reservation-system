from django import forms
from django.core import validators
from myapp.models import User
from .models import *

class Authentic(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =("username","password","first_name","last_name", 'email')




class UploadForm(forms.ModelForm):

    class Meta:
        model = seats
        fields = ['slot_name']
