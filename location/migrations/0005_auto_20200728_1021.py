# Generated by Django 3.0.8 on 2020-07-28 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_auto_20200728_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='flor',
            field=models.IntegerField(default=1, verbose_name='Этаж'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='titul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Titul', verbose_name='Титул'),
        ),
    ]
