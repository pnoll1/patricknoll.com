# Generated by Django 2.2.6 on 2019-10-28 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0007_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionfix',
            name='tax',
        ),
    ]