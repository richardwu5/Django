from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import SpecialtyPizza, SpecialtySizePrice, OtherItem, Topping, CreatePizza, Cart, Item

# Create your views here.
def pizza(request):
	if not request.user.is_authenticated:
		return render(request, "pizza/login.html", {"message": None})

	try:
		c = Cart.objects.get(user=request.user, status=Cart.OPEN)
		num_items = 0
		for i in c.items.all():
			num_items += i.quantity
	except ObjectDoesNotExist:
		c = Cart(user=request.user)
		c.save()
		num_items = 0

	if request.method == "POST":
		num_items += 1
		category = request.POST["category"]
		if (category == "specialty"):
			pizza = SpecialtyPizza.objects.get(pk=request.POST["pk"])
			name = pizza.name
			size = request.POST["size"]
			quantity = request.POST["quantity"]
			s = SpecialtySizePrice.objects.get(size = size)
			price = s.price
			try:
				item = Item.objects.get(name=name, size=size)
				item.quantity += quantity
			except ObjectDoesNotExist:
				item = Item(name=name, price=price, size=size, quantity=quantity)

			item.save()
			c.items.add(item)
		elif (category == "other"):
			pk = request.POST["pk"]
			quantity = request.POST["quantity"]
			other = OtherItem.objects.get(pk=pk)
			name = other.name
			price = other.price
			try:
				item = Item.objects.get(name=name)
				item.quantity += quantity
			except ObjectDoesNotExist:
				item = Item(name=name, price=price, quantity=quantity)

			item.save()
			c.items.add(item)
		else:
			s = request.POST["size"]
			pizza = CreatePizza.objects.get(size=s)
			size = pizza.size
			toppings = request.POST.getlist("topping_pk")
			numToppings = 0
			for t in toppings:
				numToppings += 1
			name = f"{size} Pizza"
			price = pizza.price + (numToppings * pizza.topping_price)
			item = Item(name=name, price=price, quantity=1)
			item.save()
			c.items.add(item)

		c.save()
		return HttpResponseRedirect(reverse("pizza:pizza"))

	context = get_menu()
	context["item_count"] = num_items
	return render(request, "pizza/pizza.html", context)

def specialty(request, pk):
	c = Cart.objects.get(user=request.user, status=Cart.OPEN)
	num_items = 0
	for i in c.items.all():
		num_items += i.quantity

	pizza = SpecialtyPizza.objects.get(pk=pk)
	context = {
		"pk": pizza.pk,
		"name": pizza.name,
		"category": "specialty",
		"prices": SpecialtySizePrice.objects.all(),
		"item_count": num_items
	}
	return render(request, "pizza/specialty.html", context)

def create(request):
	c = Cart.objects.get(user=request.user, status=Cart.OPEN)
	num_items = 0
	for i in c.items.all():
		num_items += i.quantity

	context = {
		"sizes": CreatePizza.objects.all(),
		"category": "create",
		"meats": Topping.objects.filter(type=Topping.MEAT),
		"veggies": Topping.objects.filter(type=Topping.VEGETABLES),
		"others": Topping.objects.filter(type=Topping.OTHERS),
		"item_count": num_items
	}
	return render(request, "pizza/create.html", context)

def other(request, pk):
	c = Cart.objects.get(user=request.user, status=Cart.OPEN)
	num_items = 0
	for i in c.items.all():
		num_items += i.quantity

	item = OtherItem.objects.get(pk=pk)
	context = {
		"pk": item.pk,
		"name": item.name,
		"description": item.description,
		"category": "other",
		"price": item.price,
		"item_count": num_items
	}
	return render(request, "pizza/other.html", context)

def get_menu():
	context = {
		"spizza": SpecialtyPizza.objects.all(),
		"spizza_prices": SpecialtySizePrice.objects.all(),
		"small": CreatePizza.objects.get(size=CreatePizza.SMALL),
		"medium": CreatePizza.objects.get(size=CreatePizza.MEDIUM),
		"large": CreatePizza.objects.get(size=CreatePizza.LARGE),
		"xlarge": CreatePizza.objects.get(size=CreatePizza.XLARGE),
		"calzone": OtherItem.objects.filter(category=OtherItem.CALZONE),
		"sandwich": OtherItem.objects.filter(category=OtherItem.SANDWICH),
		"salad": OtherItem.objects.filter(category=OtherItem.SALAD),
		"appetizer": OtherItem.objects.filter(category=OtherItem.APPETIZER),
	}
	return context

def get_cart(request):
	try:
		c = Cart.objects.get(user=request.user, status=Cart.OPEN)
	except ObjectDoesNotExist:
		return

	if request.method == "POST":
		pk = request.POST["remove"]
		item = Item.objects.get(pk=pk)
		item.delete()

	total = 0
	num_items = 0
	for i in c.items.all():
		total += i.quantity * i.price
		num_items += i.quantity

	context = {
		"items": c.items.all(),
		"total": total,
		"item_count": num_items,
	}

	return render(request, "pizza/cart.html", context)

def confirmation(request):
	c = Cart.objects.get(user=request.user, status=Cart.OPEN)
	c.status=Cart.CLOSED
	c.save()

	return render(request, "pizza/confirmation.html", {"item_count": 0})

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

def register(request):
	password = request.POST["pwd1"]
	password2 = request.POST["pwd2"]
	if (password != password2):
		return render(request, "pizza/login.html", {"message": "Your passwords do not match"})

	username = request.POST["uname"]
	if User.objects.filter(username=username).exists():
		return render(request, "pizza/login.html", {"message": "Username is already taken"})

	firstname = request.POST["fname"]
	lastname = request.POST["lname"]
	email = request.POST["email"]
	user = User.objects.create_user(username, email, password)
	user.first_name = firstname
	user.last_name = lastname
	user.save()
	login(request, user)
	return HttpResponseRedirect(reverse("pizza:pizza"))