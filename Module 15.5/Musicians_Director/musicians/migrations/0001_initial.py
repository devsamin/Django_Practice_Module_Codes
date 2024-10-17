# Generated by Django 5.1.1 on 2024-10-15 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianModel',
            fields=[
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', models.IntegerField(primary_key=True, serialize=False)),
                ('Instrument_Type', models.CharField(max_length=30)),
            ],
        ),
    ]