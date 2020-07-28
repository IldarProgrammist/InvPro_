from django.contrib import admin

from location.models import Titul, Room


@admin.register(Titul)
class Titul(admin.ModelAdmin):
    list_display = ('numberTitul','titulName')

@admin.register(Room)
class Room(admin.ModelAdmin):
    list_display = ('numberRoom','titul','flor')