# Generated by Django 3.1.1 on 2020-10-13 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '0014_auto_20201013_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=7),
        ),
    ]
