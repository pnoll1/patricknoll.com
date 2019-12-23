# Generated by Django 2.2.6 on 2019-10-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0006_auto_20191027_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.FloatField()),
                ('address', models.TextField()),
                ('zip', models.IntegerField()),
                ('state', models.TextField()),
                ('city', models.TextField()),
                ('commit', models.BooleanField()),
            ],
        ),
    ]