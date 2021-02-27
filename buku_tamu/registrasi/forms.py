from django import forms
from django.forms import ModelForm
from .models import Registrasi
from django.shortcuts import redirect, render

class Register(forms.ModelForm):
    class Meta:
        exclude = []
        model = Registrasi

    def registrasi_baru(self):
        form = Register()
        if self.POST:
            form = Register(self.POST)
            if form.is_valid():
                form.save()
                return redirect('/registrasi/tamu')
        return render(self, 'registrasi_baru.html', { 'form': form })
'''
class Edit(forms.ModelForm):
    class Meta:
        model = Registrasi
        exclude = []

    def edit_baru(self, id):
        form = Edit.Meta.model.objects.filter()
        if self.POST:
            form = Register(self.POST)
            if form.is_valid():
                form.save()
                return redirect('/registrasi/tamu')
        return render(self, 'edit_baru.html', { 'form': form })
'''