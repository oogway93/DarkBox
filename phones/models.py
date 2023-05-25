from django.db import models


class Manufacturer(models.Model):
    manufacturer = models.CharField('Производитель', max_length=30, unique=True, null=False)

    class Mete:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return f'{self.manufacturer}'


class Phone(models.Model):
    class Memory(models.IntegerChoices):
        small = 64,
        medium = 128,
        big = 256

    CHOICES = [
        (1, 'IOS'),
        (2, 'Android')
    ]

    manufacturer = models.ForeignKey('Производитель', to=Manufacturer, on_delete=models.CASCADE)
    model = models.CharField('Модель', max_length=50, null=False)
    operating_system = models.CharField('Операционная система', choices=CHOICES)
    release_year = models.DateField('Год релиза')
    memory = models.IntegerField('Память', choices=Memory.choices)

    class Mete:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

    def __str__(self):
        return f'{self.model}'
