# Generated by Django 3.1.1 on 2020-10-18 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffmodule', '0002_auto_20201011_1132'),
        ('laundry', '0007_remove_booking_delivered_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='services',
        ),
        migrations.AddField(
            model_name='booking',
            name='services',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staffmodule.service'),
        ),
    ]
