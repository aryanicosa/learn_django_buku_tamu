# Generated by Django 2.2 on 2021-02-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_urut', models.CharField(max_length=100)),
                ('nama', models.CharField(max_length=10)),
                ('alamat', models.CharField(max_length=100)),
                ('no_telpon', models.CharField(max_length=15)),
            ],
        ),
    ]
