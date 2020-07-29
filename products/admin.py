from django.contrib import admin

from products.models import Category, Firms, Models, Products, Arm


@admin.register(Category)
class RoomAdmin(admin.ModelAdmin):
     list_display = ['nameType']

@admin.register(Firms)
class FirmAdmin(admin.ModelAdmin):
     list_display = ['firmName']

@admin.register(Models)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['modelName','firm']

@admin.register(Products)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['serialNumber','modelProduct', 'category', 'location','status','ip']


@admin.register(Arm)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['nameArm','serialNamber']