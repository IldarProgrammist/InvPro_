# Generated by Django 3.0.8 on 2020-07-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0009_room_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='discription',
            field=models.TextField(blank=True, verbose_name='Премечание'),
        ),
    ]
