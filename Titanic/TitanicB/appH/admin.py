from django.contrib import admin
from . models import HousePrModel
# Register your models here.

@admin.register(HousePrModel)
class HousePrAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'area',
        'bedrooms',
        'bathrooms',
        'stories',
        'mainroad',
        'guestroom',
        'basement',
        'parking',
        'prefarea',
        'furnishingstatus',
        'luxury_item'
        ]