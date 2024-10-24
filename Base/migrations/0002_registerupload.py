# Generated by Django 4.0 on 2024-10-24 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('school', models.CharField(max_length=50)),
                ('grade', models.IntegerField()),
                ('email', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=70)),
                ('id_number', models.IntegerField()),
            ],
        ),
    ]
