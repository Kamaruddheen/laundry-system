# Generated by Django 3.1.1 on 2020-10-10 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
