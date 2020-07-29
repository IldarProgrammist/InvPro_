# Generated by Django 3.0.8 on 2020-07-29 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_room_titul'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titul',
            name='numberTitul',
        ),
        migrations.AddField(
            model_name='room',
            name='numberTitul',
            field=models.CharField(default=1, max_length=20, verbose_name='Номер титула'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='titul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Titul', verbose_name='Нахвание титула'),
        ),
        migrations.AlterField(
            model_name='titul',
            name='titulName',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название титула'),
        ),
    ]
