from django.db import models

from location.models import Room


class Category(models.Model):
    nameType = models.CharField(max_length=50, verbose_name='Категория оборудования')

    def __str__(self):
        return self.nameType

    class Meta:
        verbose_name = 'Категория оборудования'
        verbose_name_plural = 'Категории оборудования'


class Firms(models.Model):
    firmName = models.CharField(max_length=50, verbose_name='Фирма')

    def __str__(self):
        return self.firmName

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural= 'Фирмы'


class Models(models.Model):
    modelName = models.CharField(max_length=50, verbose_name='Модель')
    firm = models.ForeignKey(Firms, models.CASCADE, verbose_name='Фирма')


    def __str__(self):
        return self.modelName

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Products(models.Model):
    serialNumber = models.CharField(max_length=40, verbose_name='Серийный номер')
    modelProduct = models.ForeignKey( Models, on_delete=models.CASCADE, verbose_name='Модель')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория оборудования')
    location = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Место расположения')

    def __str__(self):
        return self.serialNumber

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'








