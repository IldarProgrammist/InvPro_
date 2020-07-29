from django.db import models

from location.models import Room
from status.models import Status


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
    ip = models.CharField(max_length=20, verbose_name='Ip-адрес', blank=True)
    location = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Место расположения')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус', blank=True)
    def __str__(self):
        return self.serialNumber

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Arm(models.Model):
    nameArm = models.CharField(max_length=100, verbose_name='Имя рабочей станции')
    serialNamber = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Серийный номер')


    def __str__(self):
        return self.nameArm

    class Meta:
        verbose_name ='Рабочая станция'
        verbose_name_plural = 'Рабочие станции'


