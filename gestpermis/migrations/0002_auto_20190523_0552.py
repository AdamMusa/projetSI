# Generated by Django 2.2.1 on 2019-05-23 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestpermis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('point', models.IntegerField(default=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='permisconducteur',
            name='capital',
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='agent',
            name='candidat',
            field=models.ManyToManyField(to='gestpermis.Candidat'),
        ),
        migrations.AlterField(
            model_name='permisconducteur',
            name='candidat',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestpermis.Candidat'),
        ),
        migrations.DeleteModel(
            name='CapitalPoint',
        ),
    ]
