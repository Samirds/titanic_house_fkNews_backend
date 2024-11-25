from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


def only_string(value):
    if not str(value).isalpha():
        raise ValidationError("value should be Alphabetic")
    return value



class TitanicModel(models.Model):
    #age = models.PositiveIntegerField(validators=[age_range])
    age = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    gender = models.CharField(max_length=6, validators=[only_string])
    fare =  models.PositiveIntegerField(validators=[MinValueValidator(1)])
    pclass = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    embarked = models.CharField(max_length=1, validators=[only_string])
    cabin = models.CharField(max_length=1, validators=[only_string])
    sbsp = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    parch = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    # def __str__(self):
    #     return self.id
