# Generated by Django 4.0.6 on 2022-11-01 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_signup_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='phone',
        ),
    ]