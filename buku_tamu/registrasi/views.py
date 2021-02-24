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

def info(request):
    return render(request, 'info.html')