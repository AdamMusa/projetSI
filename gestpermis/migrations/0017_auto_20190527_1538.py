# Generated by Django 2.2.1 on 2019-05-27 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestpermis', '0016_auto_20190527_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidat',
            name='profil',
        ),
        migrations.RemoveField(
            model_name='profilcandidat',
            name='image',
        ),
    ]
