# Generated by Django 2.2.6 on 2019-10-28 22:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0008_remove_subscriptionfix_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 28, 15, 23, 20, 235798)),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.TextField(default='santa'),
        ),
    ]
