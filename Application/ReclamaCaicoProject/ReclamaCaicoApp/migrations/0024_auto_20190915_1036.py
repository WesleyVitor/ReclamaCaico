# Generated by Django 2.2.2 on 2019-09-15 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReclamaCaicoApp', '0023_auto_20190915_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamacao',
            name='vencimento',
            field=models.DateField(default=datetime.date(2019, 9, 16)),
        ),
    ]