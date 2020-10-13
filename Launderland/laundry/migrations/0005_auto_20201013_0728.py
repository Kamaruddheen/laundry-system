# Generated by Django 3.1.1 on 2020-10-13 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0004_auto_20201012_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Booking', 'verbose_name_plural': 'Bookings'},
        ),
        migrations.AlterField(
            model_name='booking',
            name='delivery_type',
            field=models.CharField(choices=[('local', 'Pickup'), ('myself', 'Myself')], max_length=30),
        ),
    ]
