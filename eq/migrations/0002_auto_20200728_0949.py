# Generated by Django 3.0.8 on 2020-07-28 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eq', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typee',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='modelse',
            name='typeE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eq.TypeE', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='typee',
            name='nameType',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
    ]
