# Generated by Django 3.0.8 on 2020-07-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_auto_20200728_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameType', models.CharField(max_length=50, verbose_name='Тип оборудования')),
            ],
            options={
                'verbose_name': 'Тип оборудования',
                'verbose_name_plural': 'Типы оборудования',
            },
        ),
    ]
