# Generated by Django 4.2.6 on 2023-10-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarehouseManager', '0003_transporttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartransport',
            name='CarTransportType',
            field=models.CharField(choices=[('Cargo', 'Cargo'), ('Petroleum', 'Petroleum')], max_length=100),
        ),
        migrations.AlterField(
            model_name='navaltransport',
            name='NavalTransportType',
            field=models.CharField(choices=[('Cargo', 'Cargo'), ('Petroleum', 'Petroleum')], max_length=100),
        ),
    ]