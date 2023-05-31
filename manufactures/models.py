from django.db import models


class Manufacturer(models.Model):
    manufacturer = models.CharField('Производитель', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'
        db_table = 'Manufacturer'

    def __str__(self):
        return f'{self.manufacturer}'
