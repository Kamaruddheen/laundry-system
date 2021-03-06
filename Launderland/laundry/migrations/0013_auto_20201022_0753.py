# Generated by Django 3.1.1 on 2020-10-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0012_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('pending', 'Pending'), ('cleaning', 'Cleaning'), ('pickedup', 'Picked Up'), ('canceled', 'Canceled'), ('ready', 'Ready'), ('delivered', 'Delivered')], default='New', max_length=20),
        ),
    ]
