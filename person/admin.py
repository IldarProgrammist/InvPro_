from django.contrib import admin

from person.models import Person


@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = ('firstName','lastName','fatherName', 'phone')
