from django.db import models


class Titul(models.Model):
    numberTitul = models.CharField(max_length=4, verbose_name='номер титула', unique=True )
    titulName = models.CharField(max_length=100, verbose_name='название титула', unique=True)

    def __str__(self):
        return self.titulName

    class Meta:
        verbose_name  = 'Титул'
        verbose_name_plural = 'Титулы'

class Room(models.Model):
    numberRoom = models.CharField(max_length=10, verbose_name='Номер кабинета', unique=True)
    titul = models.ForeignKey(Titul, on_delete=models.CASCADE, verbose_name='Титул')
    flor = models.IntegerField(verbose_name='Этаж')

    def __str__(self):
        return self.numberRoom

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural  = 'Кабинеты'








