# Generated by Django 4.2.1 on 2023-05-26 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_alter_phone_manufacturer'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='manufacturer',
            table='Manufacturer',
        ),
        migrations.AlterModelTable(
            name='phone',
            table='Phone',
        ),
    ]