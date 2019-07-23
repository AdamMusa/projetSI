# Generated by Django 2.2.1 on 2019-05-23 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestpermis', '0003_auto_20190523_0555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='permis',
        ),
        migrations.AddField(
            model_name='categorie',
            name='permis',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestpermis.PermisConducteur'),
            preserve_default=False,
        ),
    ]