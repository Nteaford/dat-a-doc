# Generated by Django 4.0.1 on 2022-01-21 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image_url',
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
    ]
