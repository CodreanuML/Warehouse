# Generated by Django 4.2.6 on 2023-10-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarehouseManager', '0006_alter_cartransport_route_alter_navaltransport_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_routes',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='naval_routes',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]