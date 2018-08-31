from django.db import models

# Create your models here.
class SpecialtyPizza(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

class OtherItem(models.Model):
    CALZONE = "CZ"
    SANDWICH = "SW"
    SALAD = "SL"
    APPETIZER = "AP"
    CATEGORY_CHOICES = (
        (CALZONE, "Calzone"),
        (SANDWICH, "Sandwich"),
        (SALAD, "Salad"),
        (APPETIZER, "Appetizer"),
    )
    name = models.CharField(max_length=64)
    category = models.CharField(
        max_length=64,
        choices=CATEGORY_CHOICES,
        default=SANDWICH,
    )
    description = models.CharField(max_length=256, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Price(models.Model):
    SPECIALTY = "SP"
    REGULAR = "RG"
    TOPPINGS = "TP"
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    XLARGE = "XL"
    CATEGORY_CHOICES = (
        (SPECIALTY, "Specialty Pizza"),
        (REGULAR, "Create Your Own Pizza"),
        (TOPPINGS, "Toppings"),
    )
    category = models.CharField(
        max_length=8,
        choices=CATEGORY_CHOICES,
        default=SPECIALTY,
    )
    SIZE_CHOICES = (
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large"),
        (XLARGE, "Extra Large"),
    )
    size = models.CharField(
        max_length=64,
        choices=SIZE_CHOICES,
        default=SMALL,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Topping(models.Model):
    MEAT = "M"
    VEGETABLES = "V"
    OTHERS = "O"
    TYPE_CHOICES = (
        (MEAT, "Meat"),
        (VEGETABLES, "Vegetables"),
        (OTHERS, "Others"),
    )
    name = models.CharField(max_length=32)
    type = models.CharField(
        max_length=16,
        choices=TYPE_CHOICES,
        default=MEAT,
    )