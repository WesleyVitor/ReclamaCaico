# Generated by Django 2.2.2 on 2019-09-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReclamaCaicoApp', '0010_comentario_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='user',
        ),
        migrations.AddField(
            model_name='comentario',
            name='nome',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
