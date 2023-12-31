# Generated by Django 4.2.6 on 2023-10-28 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CarTransport',
            fields=[
                ('transport_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WarehouseManager.transport')),
                ('CarTransportType', models.CharField(choices=[('Cargo', 'Cargo'), ('Petroleum', 'Petroleum'), ('For Persons', 'For Persons')], max_length=100)),
                ('Parked', models.BooleanField()),
                ('Route', models.CharField(choices=[('Draganesti-Constanta', 'Cargo')], max_length=100)),
            ],
            bases=('WarehouseManager.transport',),
        ),
        migrations.CreateModel(
            name='NavalTransport',
            fields=[
                ('transport_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WarehouseManager.transport')),
                ('NavalTransportType', models.CharField(choices=[('Cargo', 'Cargo'), ('Petroleum', 'Petroleum'), ('For Persons', 'For Persons')], max_length=100)),
                ('Docked', models.BooleanField()),
                ('Route', models.CharField(choices=[('Shanghai-Chaina', 'Cargo')], max_length=100)),
            ],
            bases=('WarehouseManager.transport',),
        ),
    ]
