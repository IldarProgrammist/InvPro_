# Generated by Django 3.0.8 on 2020-07-29 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20200729_0810'),
        ('person', '0009_person_organization'),
        ('act', '0003_act'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extradition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateExtradition', models.DateField(auto_now_add=True, verbose_name='Дата выдачи')),
                ('numberAct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='act.Act', verbose_name='Акт')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Person', verbose_name='Пользователь')),
                ('serialNumberProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products', verbose_name='серийный номер')),
            ],
            options={
                'verbose_name': 'Выдача оборудования',
                'verbose_name_plural': 'Выдача оборудования',
            },
        ),
    ]
