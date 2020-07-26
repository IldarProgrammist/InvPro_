from django.db import models

class Position(models.Model):
    positionName = models.CharField(max_length=30, verbose_name='Название должности')

    def __str__(self):
        return self.positionName

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'



class Department(models.Model):
    depName = models.CharField(max_length=50, verbose_name='Название отдела')

    def __str__(self):
        return self.depName

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'



class Person(models.Model):
    firstName = models.CharField(max_length=20, verbose_name='Фамилия')
    lastName = models.CharField(max_length=20, verbose_name='Имя')
    fatherName = models.CharField(max_length=20, verbose_name='Отчество')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    photo = models.ImageField( blank=True)
    depatName = models.ForeignKey(Department, models.CASCADE, verbose_name='Отдел')
    position = models.ForeignKey(Position,    models.CASCADE, verbose_name='Должность')
    email = models.EmailField(verbose_name='Электронная почта', blank=True)

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
