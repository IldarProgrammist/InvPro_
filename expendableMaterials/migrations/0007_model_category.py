# Generated by Django 3.0.8 on 2020-07-29 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expendableMaterials', '0006_materials'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='expendableMaterials.CategoryMaterial', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
