# Generated by Django 2.2 on 2021-02-26 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrasi', '0002_auto_20210225_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrasi',
            name='no_urut',
        ),
    ]