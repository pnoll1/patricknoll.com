# Generated by Django 2.2.9 on 2020-01-15 23:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0010_auto_20200115_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 15, 8, 38, 710043)),
        ),
    ]
