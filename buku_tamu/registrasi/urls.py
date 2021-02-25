from django.urls import path
from . import views


urlpatterns = [
    path('tamu', views.tamu),
    path('registrasi', views.registrasi),
    path('info', views.info),
    path('hapus/<int:id>', views.hapus),
    path('edit/<int:id>', views.form_edit)
]