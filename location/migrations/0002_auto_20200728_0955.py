# Generated by Django 3.0.8 on 2020-07-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titul',
            name='numberTitul',
            field=models.CharField(max_length=4, unique=True, verbose_name='номер титула'),
        ),
        migrations.AlterField(
            model_name='titul',
            name='titulName',
            field=models.CharField(max_length=100, unique=True, verbose_name='название титула'),
        ),
    ]
