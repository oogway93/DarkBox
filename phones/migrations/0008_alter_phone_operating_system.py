# Generated by Django 4.2.1 on 2023-05-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0007_alter_manufacturer_table_alter_phone_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='operating_system',
            field=models.CharField(choices=[('IOS', 'IOS'), ('Android', 'A')], verbose_name='Операционная система'),
        ),
    ]
