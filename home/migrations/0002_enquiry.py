# Generated by Django 4.0.6 on 2022-10-13 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=200)),
                ('Dates', models.DateField(auto_now_add=False, auto_now=False, blank=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
