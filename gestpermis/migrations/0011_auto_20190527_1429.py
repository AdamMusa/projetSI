# Generated by Django 2.2.1 on 2019-05-27 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestpermis', '0010_auto_20190527_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidat',
            old_name='User',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='candidat',
            name='email',
        ),
        migrations.RemoveField(
            model_name='candidat',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='candidat',
            name='prenom',
        ),
    ]
