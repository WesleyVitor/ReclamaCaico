# Generated by Django 2.2.2 on 2019-09-15 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReclamaCaicoApp', '0024_auto_20190915_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamacao',
            name='vencimento',
            field=models.DateField(default=datetime.date(2019, 10, 15)),
        ),
    ]
