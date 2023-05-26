# Generated by Django 4.2.1 on 2023-05-26 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_operating_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='manufacturer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='phones.manufacturer'),
            preserve_default=False,
        ),
    ]
