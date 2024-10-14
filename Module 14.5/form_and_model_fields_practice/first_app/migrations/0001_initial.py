# Generated by Django 5.1.1 on 2024-10-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date_time', models.DateField()),
                ('decimal_field', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]