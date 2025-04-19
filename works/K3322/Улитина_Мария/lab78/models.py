from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    TYPE = [
        ('Main', 'Основные услуги'),
        ('Dop', 'Дополнительные услуги'),
    ]

    type = models.CharField(choices=TYPE, max_length=4, default='Main', verbose_name='Категория услуг')

    def __str__(self):
        return self.title


