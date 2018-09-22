from django.contrib import admin

from .models import SpecialtySizePrice, SpecialtyPizza, OtherItem, Topping, CreatePizza, Cart, Item

# Register your models here.
admin.site.register(SpecialtySizePrice)
admin.site.register(SpecialtyPizza)
admin.site.register(OtherItem)
admin.site.register(Topping)
admin.site.register(CreatePizza)
admin.site.register(Cart)
admin.site.register(Item)
