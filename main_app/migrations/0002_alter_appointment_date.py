# Generated by Django 3.2.9 on 2022-01-18 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default='%m/%d/%y %H:%M'),
        ),
    ]