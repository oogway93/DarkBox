# Generated by Django 4.2.1 on 2023-05-26 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0010_alter_phone_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone',
            options={'ordering': ['id'], 'verbose_name': 'Phone', 'verbose_name_plural': 'Phones'},
        ),
    ]
