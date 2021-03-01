from django.urls import path
from . import views, forms


urlpatterns = [
    path('tamu', views.tamu),
    #path('registrasi', views.registrasi), # sudah diganti regitrasi dengan forms.py
    path('info', views.info),
    path('hapus/<int:id>', views.hapus),
    path('edit/<int:id>', views.form_edit),
    path('registrasi', forms.Register.registrasi),
    #path('edit_baru/<int:id>', forms.Edit.edit_baru)
]