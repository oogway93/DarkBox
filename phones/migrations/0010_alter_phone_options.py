# Generated by Django 4.2.1 on 2023-05-26 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0009_alter_phone_operating_system'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone',
            options={'ordering': ['-id'], 'verbose_name': 'Phone', 'verbose_name_plural': 'Phones'},
        ),
    ]