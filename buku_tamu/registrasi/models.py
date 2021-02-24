from django.db import models

# Create your models here.
class Registrasi(models.Model):
    no_urut = models.CharField(max_length=100)
    nama = models.CharField(max_length=10)
    alamat = models.CharField(max_length=100)
    no_telpon = models.CharField(max_length=15)