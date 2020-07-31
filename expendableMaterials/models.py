from django.db import models

from products.models import Models
from status.models import Status


class Firm(models.Model):
    name = models.CharField(max_length=50, verbose_name='Фирма')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'



class Color(models.Model):
    name = models.CharField(max_length=30, verbose_name='Цвет', unique=True)
    word = models.CharField(max_length=1, verbose_name='Обозначение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'



class CategoryMaterial(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Котегория расходного материала'
        verbose_name_plural = 'Категория расходных материалов'



class Model(models.Model):
    name = models.CharField(max_length=50, verbose_name='Модель', unique=True)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name='Производитель')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет', blank=True)
    img = models.ImageField(verbose_name='фото модели', blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class PrinterModel(models.Model):
    number = models.CharField(max_length=4, verbose_name="Номер", unique=True)
    printer = models.ForeignKey(Models, on_delete=models.CASCADE, verbose_name='Модель принтера')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name='Модель картриджа')


    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Модель принтера'
        verbose_name_plural = 'Модели принтеров'



class Materials(models.Model):
    serialNumber = models.CharField(max_length=30, verbose_name='Серийный номер', unique=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name='Модель')
    category = models.ForeignKey(CategoryMaterial, on_delete=models.CASCADE, verbose_name='Категория')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')

    def __str__(self):
        return self.serialNumber


    class Meta:
        verbose_name = 'Расходный материал'
        verbose_name_plural = 'Расходные материалы'



