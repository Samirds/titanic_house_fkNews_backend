from rest_framework import serializers
from . models import HousePrModel
from django.core.exceptions import ValidationError


class HousePriSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePrModel
        fields = '__all__'
