# Generated by Django 2.2.2 on 2019-09-09 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReclamaCaicoApp', '0016_auto_20190909_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamacao',
            name='foto',
        ),
    ]
