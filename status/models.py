from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название статуса')
    img = models.ImageField(verbose_name='Картинка статуса', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Статус'
        verbose_name_plural = 'Статусы'
