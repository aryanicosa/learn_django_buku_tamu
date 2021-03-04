from django import forms
from django.forms import ModelForm
from .models import Registrasi
from django.shortcuts import redirect, render
from . import models

# membuat form dari model yang sudah ada di models.py dan terhubung dengan postgresql
# melalui settings.py
class Register(forms.ModelForm):
    class Meta:
        exclude = ['id']
        model = Registrasi