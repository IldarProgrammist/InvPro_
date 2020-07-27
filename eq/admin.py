from django.contrib import admin

from eq.models import TypeE, FirmsE, ModelsE


@admin.register(TypeE)
class TypeEq(admin.ModelAdmin):
    list_display = ['nameType']

@admin.register(FirmsE)
class FirmEq(admin.ModelAdmin):
    list_display = ['firmName']


@admin.register(ModelsE)
class  ModelEq(admin.ModelAdmin):
    list_display = ['modelName','firm','typeE']


