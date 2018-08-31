from django.contrib import admin
from .models import SpecialtyPizza, OtherItem, Price, Topping

# Register your models here.
admin.site.register(SpecialtyPizza)
admin.site.register(OtherItem)
admin.site.register(Price)
admin.site.register(Topping)