from django.db import models
# from phones.models import Phone
from phones.models import Manufacturer


class Laptop(models.Model):
    CHOICES = [
        [("IOS", "IOS"),
         ("Windows", "Windows"),
         ("Linux", "Linux")],

        [(256, 256),
         (512, 512),
         (1024, 1024)]
    ]

    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.CASCADE)
    operating_system: tuple[str] = models.CharField('Операционная система', choices=CHOICES[0])
    model: str = models.CharField('Модель', max_length=50)
    release_year = models.DateField('Год релиза')
    memory: tuple[int] = models.IntegerField('Память', choices=CHOICES[1])
    color: str = models.CharField('Цвет', max_length=50, default='Grey')
    price: int = models.IntegerField('Цена', null=True, blank=True)
    delivery: int = models.IntegerField('Доставка', default=0)
    is_out_of_stocks = models.BooleanField('Есть ли в наличии', default=True)

    class Meta:
        verbose_name = 'Laptop'
        verbose_name_plural = 'Laptops'
        db_table = 'Laptop'
        ordering = ['id']

    def __str__(self):
        return f'{self.manufacturer}: {self.model}'
