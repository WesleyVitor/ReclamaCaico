# Generated by Django 2.2.2 on 2019-09-03 22:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ReclamaCaicoApp', '0003_reclamacao_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamacao',
            name='user',
        ),
        migrations.AddField(
            model_name='reclamacao',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
