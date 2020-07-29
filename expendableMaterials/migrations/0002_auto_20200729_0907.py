# Generated by Django 3.0.8 on 2020-07-29 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expendableMaterials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Фирма')),
            ],
            options={
                'verbose_name': 'Фирма',
                'verbose_name_plural': 'Фирмы',
            },
        ),
        migrations.AlterModelOptions(
            name='categorymaterial',
            options={'verbose_name': 'Котегория расходного материала', 'verbose_name_plural': 'Категория расходных материалов'},
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Модель')),
                ('color', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='expendableMaterials.Color', verbose_name='Цвет')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expendableMaterials.Firm', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
    ]
