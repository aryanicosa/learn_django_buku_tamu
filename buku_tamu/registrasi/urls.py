from django.urls import path
from . import views, forms


urlpatterns = [
    path('tamu', views.tamu),
    path('registrasi', views.registrasi), 
    path('info', views.info),
    path('hapus/<int:id>', views.hapus),
    path('edit/<int:id>', views.edit),
    
    #dibawah ini menggunakan cara plain html
    #path('edit_form/<int:id>', views.edit_form),
    #path('registrasi', viewa.registrasi_form),
]