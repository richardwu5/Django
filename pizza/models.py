from django.db import models
from django.conf import settings


# Create your models here.
class SpecialtySizePrice(models.Model):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    XLARGE = "XL"
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

    def __str__(self):
        return f"{self.size} for ${self.price}"

class SpecialtyPizza(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256, blank=True, null=True)
    size = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


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

    def __str__(self):
        return f"{self.name}"


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

    def __str__(self):
        return f"{self.name}"

class CreatePizza(models.Model):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"
    XLARGE = "XL"
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
    topping_price = models.DecimalField(max_digits=10, decimal_places=2)
    toppings = models.ManyToManyField(Topping, blank=True, related_name="createpizza")

    def __str__(self):
        return f"{self.size} for ${self.price}. Each additional topping for {self.topping_price}"

class Item(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(max_length=100)
    size = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} {self.name} at {self.price}"

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    OPEN = "O"
    CLOSED = "C"
    STATUS_CHOICES = (
        (OPEN, "Open"),
        (CLOSED, "Closed"),
    )
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=OPEN,
    )
    items = models.ManyToManyField(Item, blank=True, related_name="cart")

    def __str__(self):
        return f"{self.status} cart for {self.user}"
