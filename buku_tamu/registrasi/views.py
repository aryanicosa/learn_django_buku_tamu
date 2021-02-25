from django.shortcuts import redirect, render

from .models import Registrasi

# Create your views here.
def tamu(request):
    data = Registrasi.objects.all()
    return render(request, 'tamu.html', {'data': data})

def registrasi(request):
    if request.POST:
        Registrasi.objects.create(
            no_urut = request.POST['no_urut'],
            nama = request.POST['nama'],
            alamat = request.POST['alamat'],
            no_telpon = request.POST['no_telpon'],
        )
        return redirect('/registrasi/tamu')
    return render(request, 'registrasi.html')

def hapus(request, id):
    baris = Registrasi.objects.get(id=id)
    baris.delete()
    return redirect('/registrasi/tamu')

def form_edit(request, id):
    data = Registrasi.objects.get(id=id)
    if request.POST:
        Registrasi.objects.filter(pk=id).update(
            nama = request.POST['nama'],
            alamat = request.POST['alamat'],
            no_telpon = request.POST['no_telpon'],
        )
        return redirect('/registrasi/tamu')
    return render(request, 'edit.html', {'data': data})
    

def info(request):
    return render(request, 'info.html')