# Generated by Django 4.2.1 on 2023-05-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0012_alter_phone_memory'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='color',
            field=models.CharField(default='Black', max_length=50, verbose_name='Цвет'),
        ),
    ]
