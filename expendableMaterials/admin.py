from django.contrib import admin

from expendableMaterials.models import *

@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name','word')


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name','firm','color')

@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('serialNumber','model','status','category', 'date_z')


@admin.register(PrinterModel)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('number','printer','model')