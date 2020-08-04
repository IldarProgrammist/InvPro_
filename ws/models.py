from django.db import models

class workspase(models.Model):
    nameComputar = models.CharField(max_length=40, verbose_name='Имя компьютера')