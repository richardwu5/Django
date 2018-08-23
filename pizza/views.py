from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def pizza(request):
	if not request.user.is_authenticated:
		return render(request, "pizza/login.html", {"message": None})
	context = {
		"user": request.user
	}
	return render(request, "pizza/pizza.html", context)

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