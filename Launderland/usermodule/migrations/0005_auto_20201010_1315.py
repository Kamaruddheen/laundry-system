# Generated by Django 3.1.1 on 2020-10-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0004_auto_20201010_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]
