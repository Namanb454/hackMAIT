# Generated by Django 4.0.6 on 2022-11-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_bookanappointment_appointment_bookanapointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]