from django.db import models

from person.models import Person
from products.models import Category, Products


class Application(models.Model):
    number = models.CharField(max_length=30, verbose_name='Номер заявки', unique=True)
    fistsName = models.ForeignKey(Person,verbose_name='Пользователь', on_delete=models.CASCADE)
    discription = models.TextField(verbose_name='Описание заявки')
    date_created = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_performed = models.BooleanField(verbose_name='Выполнена')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Act(models.Model):
    numberAct = models.CharField(max_length=20, verbose_name='Номер акта', unique=True)
    namberApplication = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name='Заявка')
    scan = models.ImageField(verbose_name='Скан подписанного акта', blank=True)

    def __str__(self):
        return self.numberAct

    class Meta:
        verbose_name = 'Акт'
        verbose_name_plural = 'Акты'



class Extradition(models.Model):
    discription = models.CharField(max_length=20, verbose_name='Заголовок')
    numberAct = models.ForeignKey(Act, on_delete=models.CASCADE, verbose_name='Акт')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Пользователь')
    serialNumberProduct = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='серийный номер')
    dateExtradition = models.DateField(auto_now_add=True, verbose_name='Дата выдачи')

    def __str__(self):
        return self.discription


    class Meta:
        verbose_name = 'Выдача оборудования'
        verbose_name_plural = 'Выдача оборудования'
