# Generated by Django 2.2.6 on 2019-10-28 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0004_auto_20191027_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionfix',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]