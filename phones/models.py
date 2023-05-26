from django.db import models


class Manufacturer(models.Model):
    manufacturer = models.CharField('Производитель', max_length=30, unique=True, null=False)

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'
        db_table = 'Manufacturer'

    def __str__(self):
        return f'{self.manufacturer}'


class Phone(models.Model):
    CHOICES = [
        [(1, 'IOS'),
         (2, 'Android')],

        [(1, 64),
         (2, 128),
         (3, 256)]
    ]

    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.CASCADE)
    model = models.CharField('Модель', max_length=50, null=False)
    operating_system = models.CharField('Операционная система', choices=CHOICES[0])
    release_year = models.DateField('Год релиза')
    memory = models.IntegerField('Память', choices=CHOICES[1])

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'
        db_table = 'Phone'

    def __str__(self):
        return f'{self.model}'
