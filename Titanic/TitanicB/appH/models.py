from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class HousePrModel(models.Model):
    area = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    bedrooms = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    bathrooms = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    stories = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    mainroad = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    guestroom = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    basement = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    parking = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    prefarea = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    furnishingstatus = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    luxury_item = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])

