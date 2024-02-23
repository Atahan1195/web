# Generated by Django 5.0.2 on 2024-02-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('people_number', models.PositiveSmallIntegerField()),
                ('message', models.TextField(blank=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
