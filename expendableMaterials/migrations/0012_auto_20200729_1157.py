# Generated by Django 3.0.8 on 2020-07-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expendableMaterials', '0011_printermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printermodel',
            name='number',
            field=models.CharField(max_length=4, unique=True, verbose_name='Номер'),
        ),
    ]
