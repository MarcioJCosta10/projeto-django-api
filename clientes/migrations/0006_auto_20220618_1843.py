# Generated by Django 3.1.2 on 2022-06-18 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20220618_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 18, 18, 43, 46, 36623)),
        ),
    ]
