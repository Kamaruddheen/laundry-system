# Generated by Django 3.1.1 on 2020-10-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0009_auto_20201010_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='staff_status',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
