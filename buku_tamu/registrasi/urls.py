from django.urls import path
from . import views

urlpatterns = [
    path('tamu', views.tamu),
    path('registrasi', views.registrasi),
    path('info', views.info),
]