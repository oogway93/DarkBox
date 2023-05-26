# Generated by Django 4.2.1 on 2023-05-26 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_alter_manufacturer_options_alter_phone_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.manufacturer', verbose_name='Производитель'),
        ),
    ]
