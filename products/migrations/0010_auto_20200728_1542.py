# Generated by Django 3.0.8 on 2020-07-28 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='modelProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Models', verbose_name='Модель'),
        ),
    ]
