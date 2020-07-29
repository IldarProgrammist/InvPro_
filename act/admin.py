from django.contrib import admin

from act.models import Application, Act, Extradition


@admin.register(Application)
class  ApplicationAdmin(admin.ModelAdmin):
    list_display = ['number','discription','date_created','fistsName']

@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    list_display = ['numberAct','namberApplication']

@admin.register(Extradition)
class ExtraditionAdmin(admin.ModelAdmin):
    list_display = ['numberAct','person','serialNumberProduct', 'dateExtradition']
