from django.urls import path
from . import views

# Create your views here.
app_name = "pizza"
urlpatterns = [
	path("", views.pizza, name="pizza"),
	path("/create", views.create, name="create"),
	path("/<name>", views.specialty, name="specialty"),
	path("login", views.login_view, name="login"),
	path("logout", views.logout_view, name="logout")	
]