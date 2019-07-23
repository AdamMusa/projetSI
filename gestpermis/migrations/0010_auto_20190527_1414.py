# Generated by Django 2.2.1 on 2019-05-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestpermis', '0009_auto_20190527_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidat',
            old_name='user',
            new_name='User',
        ),
        migrations.AddField(
            model_name='candidat',
            name='nom',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidat',
            name='prenom',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]