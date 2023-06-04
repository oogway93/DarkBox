from django.db import models


class Manufacturer(models.Model):
    manufacturer = models.CharField('Производитель', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'
        db_table = 'Manufacturer'

    def __str__(self):
        return f'{self.manufacturer}'


class Phone(models.Model):
    CHOICES = [
        [("IOS", "IOS"),
         ("Android", "Android")],

        [(64, 64),
         (128, 128),
         (256, 256)]
    ]

    manufacturer: str = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.CASCADE)
    model: str = models.CharField('Модель', max_length=50, null=False)
    operating_system: list[str] = models.CharField('Операционная система', choices=CHOICES[0])
    release_year = models.DateField('Год релиза')
    memory: int = models.IntegerField('Память', choices=CHOICES[1])
    color: str = models.CharField('Цвет', max_length=50, default='Black')
    price: int = models.IntegerField('Цена', null=True, blank=True)
    delivery: int = models.IntegerField('Доставка', default=0)
    is_out_of_stocks = models.BooleanField('Есть ли в наличии', default=True)

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'
        db_table = 'Phone'
        ordering = ['id']

    def __str__(self):
        return f'{self.manufacturer}: {self.model}'
