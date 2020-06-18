from django.db import models
from django.contrib.auth.models import User
from sortedm2m.fields import SortedManyToManyField
from enum import Enum

class IngestionType(Enum):
    BREAKFAST = "BREAKFAST"
    DINNER = "DINNER"
    SNACK ="SNACK"

class Dish(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.TextField()

class Ingestion(models.Model):
    name = models.CharField(max_length=512)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=256, choices=[(tag, tag.value) for tag in IngestionType])
    calories = models.IntegerField()
    fats = models.IntegerField()
    proteins = models.IntegerField()
    carbohydrates = models.IntegerField()
    dish_name = models.CharField(max_length=100)
    dish_recipe = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    calories_per_100g = models.IntegerField()
    weight_in_gramms = models.IntegerField()
    fats_per_100g = models.IntegerField()
    proteins_per_100g = models.IntegerField()
    carbohydrates_per_100g = models.IntegerField()

class ListOfProducts(models.Model):
    list_of_products = models.ManyToManyField(Product)

class ParamsOfHike(models.Model):
    products = models.ForeignKey(ListOfProducts, on_delete=models.CASCADE)
    ingestions = SortedManyToManyField(Ingestion)
    days = models.IntegerField()    
    people = models.IntegerField()

class Distribution(models.Model):
    pass
