# Generated by Django 3.0.8 on 2020-07-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20200729_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Название статуса'),
        ),
    ]