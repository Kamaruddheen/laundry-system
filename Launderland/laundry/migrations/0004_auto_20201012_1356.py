# Generated by Django 3.1.1 on 2020-10-12 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0003_auto_20201012_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='load_type',
            field=models.CharField(choices=[('bag', 'Bag'), ('dress', 'Dress')], max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='unit',
            field=models.PositiveIntegerField(),
        ),
    ]
