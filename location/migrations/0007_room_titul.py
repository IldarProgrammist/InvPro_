# Generated by Django 3.0.8 on 2020-07-28 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0006_auto_20200728_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberTitul', models.CharField(max_length=4, unique=True, verbose_name='номер титула')),
                ('titulName', models.CharField(max_length=100, unique=True, verbose_name='название титула')),
            ],
            options={
                'verbose_name': 'Титул',
                'verbose_name_plural': 'Титулы',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberRoom', models.CharField(max_length=10, unique=True, verbose_name='Номер кабинета')),
                ('flor', models.IntegerField(verbose_name='Этаж')),
                ('titul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Titul', verbose_name='Титул')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеты',
            },
        ),
    ]
