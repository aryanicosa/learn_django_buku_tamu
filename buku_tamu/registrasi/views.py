from django.shortcuts import redirect, render
from .models import Registrasi
from .forms import Register

def tamu(request):
    data = Registrasi.objects.all()
    return render(request, 'tamu.html', {'data': data})

def registrasi(request):
    form = Register()
    if request.POST:
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/registrasi/tamu')
    return render(request, 'registrasi.html', { 'form': form })

def edit(request, id):
    data = Registrasi.objects.get(id=id)
    form = Register(instance=data)
    if request.POST:
        form = Register(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/registrasi/tamu')
    return render(request, 'edit.html', {'form': form})

def hapus(request, id):
    Registrasi.objects.get(id=id).delete()
    return redirect('/registrasi/tamu')

def info(request):
    return render(request, 'info.html')

''' Sudah diganti menggunakan form
def registrasi_form(request):
    if request.POST:
        Registrasi.objects.create(
            nama = request.POST['nama'],
            alamat = request.POST['alamat'],
            no_telpon = request.POST['no_telpon'],
        )
        return redirect('/registrasi/tamu')
    return render(request, 'registrasi.html')
'''

''' Sudah diganti menggunakan form 
def edit_form(request, id):
    data = Registrasi.objects.get(id=id)
    if request.POST:
        Registrasi.objects.filter(pk=id).update(
            nama = request.POST['nama'],
            alamat = request.POST['alamat'],
            no_telpon = request.POST['no_telpon'],
        )
        return redirect('/registrasi/tamu')
    return render(request, 'edit.html', {'data': data})
'''