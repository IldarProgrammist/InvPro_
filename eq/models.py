from django.db import models

from django.db import models

class TypeE(models.Model):
    nameType = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.nameType

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class FirmsE(models.Model):
    firmName = models.CharField(max_length=50, verbose_name='Фирма')

    def __str__(self):
        return self.firmName

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural= 'Фирмы'

class ModelsE(models.Model):
    modelName = models.CharField(max_length=50, verbose_name='Модель')
    firm = models.ForeignKey(FirmsE, models.CASCADE, verbose_name='Фирма')
    typeE = models.ForeignKey(TypeE, models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.modelName

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'








