from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import SpecialtyPizza, OtherItem, Price, Topping

# Create your views here.
def pizza(request):
	if not request.user.is_authenticated:
		return render(request, "pizza/login.html", {"message": None})

	context = {
		"spizza": SpecialtyPizza.objects.all(),
		"spizza_prices": Price.objects.filter(category=Price.SPECIALTY),
		"small_price":
			{
				"pizza_price": Price.objects.get(category=Price.REGULAR, size=Price.SMALL),
				"topping_price": Price.objects.get(category=Price.TOPPINGS, size=Price.SMALL)
			},
		"medium_price":
			{
				"pizza_price": Price.objects.get(category=Price.REGULAR, size=Price.MEDIUM),
				"topping_price": Price.objects.get(category=Price.TOPPINGS, size=Price.MEDIUM)
			},
		"large_price":
			{
				"pizza_price": Price.objects.get(category=Price.REGULAR, size=Price.LARGE),
				"topping_price": Price.objects.get(category=Price.TOPPINGS, size=Price.LARGE)
			},
		"xlarge_price":
			{
				"pizza_price": Price.objects.get(category=Price.REGULAR, size=Price.XLARGE),
				"topping_price": Price.objects.get(category=Price.TOPPINGS, size=Price.XLARGE)
			},
		"calzone": OtherItem.objects.filter(category=OtherItem.CALZONE),
		"sandwich": OtherItem.objects.filter(category=OtherItem.SANDWICH),
		"salad": OtherItem.objects.filter(category=OtherItem.SALAD),
		"appetizer": OtherItem.objects.filter(category=OtherItem.APPETIZER),
	}
	return render(request, "pizza/pizza.html", context)

def specialty(request, name):
	context = {
		"name": name,
		"prices": Price.objects.filter(category=Price.SPECIALTY)
	}
	return render(request, "pizza/specialty.html", context)

def create(request):
	context = {
		"prices": Price.objects.filter(category=Price.REGULAR),
		"meats": Topping.objects.filter(type=Topping.MEAT),
		"veggies": Topping.objects.filter(type=Topping.VEGETABLES),
		"others": Topping.objects.filter(type=Topping.OTHERS),
	}
	return render(request, "pizza/create.html", context)

def login_view(request):
	#Add try, except later
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("pizza:pizza"))
	else:
		return render(request, "pizza/login.html", {"message": "Invalid credentials"})

def logout_view(request):
	logout(request)
	return render(request, "pizza/login.html", {"message": "Logged out"})