# Generated by Django 2.2.1 on 2019-05-27 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestpermis', '0012_auto_20190527_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidat',
            old_name='data',
            new_name='data_burth',
        ),
    ]