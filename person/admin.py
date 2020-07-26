from django.contrib import admin

from person.models import Person, Department, Position


@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = ('firstName','lastName','fatherName', 'phone','depatName','position')

@admin.register(Department)
class Depatment(admin.ModelAdmin):
    list_display = ['depName']


@admin.register(Position)
class  Position(admin.ModelAdmin):
    list_display = ['positionName']



