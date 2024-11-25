from rest_framework import serializers
from . models import TitanicModel
from django.core.exceptions import ValidationError


class TitanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitanicModel
        # fields = ['id', 'age', 'gender', 'fare', 'pclass', 'embarked', 'cabin', 'family']
        fields = '__all__'


        # def validate(self, obj):
        #     # if obj['age'] <0:
        #     #     raise serializers.ValidationError("age mmust be >0")
        #     return obj
