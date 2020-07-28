# Generated by Django 3.0.8 on 2020-07-28 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_room_titul'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNamber', models.CharField(max_length=20, verbose_name='Серийный номер')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category', verbose_name='Категория')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Room', verbose_name='Место расположение')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Models', verbose_name='Модель')),
            ],
        ),
    ]