from django.contrib import admin
from . models import TitanicModel
# Register your models here.

@admin.register(TitanicModel)
class TitanicAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'gender', 'fare', 'pclass', 'embarked', 'cabin', 'sbsp', 'parch']