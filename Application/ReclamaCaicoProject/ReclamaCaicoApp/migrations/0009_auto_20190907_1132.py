# Generated by Django 2.2.2 on 2019-09-07 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReclamaCaicoApp', '0008_auto_20190907_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
