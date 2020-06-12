from django.db import models
from django.contrib.auth.models import User
from enum import Enum

class IngestionType(Enum):
    BREAKFEST = "BREAKFEST"
    DINNER = "DINNER"
    SNACK ="SNACK"

class Ingestion(models.Model):
    name = models.CharField(max_length=512)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=256, choices=[(tag, tag.value) for tag in IngestionType])
    calories = models.IntegerField()
    fats = models.IntegerField()
    proteins = models.IntegerField()
    carbohydrates = models.IntegerField()
