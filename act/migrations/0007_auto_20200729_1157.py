# Generated by Django 3.0.8 on 2020-07-29 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('act', '0006_auto_20200729_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extradition',
            name='numberAct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='act.Act', verbose_name='Акт'),
        ),
    ]
