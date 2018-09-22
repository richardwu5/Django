from django.urls import path
from . import views

# Create your views here.
app_name = "pizza"
urlpatterns = [
	path("", views.pizza, name="pizza"),
	path("create", views.create, name="create"),
	path("other/<pk>", views.other, name="other"),
	path("login", views.login_view, name="login"),
	path("logout", views.logout_view, name="logout"),
	path("specialty/<pk>", views.specialty, name="specialty"),
	path("register", views.register, name="register"),
	path("cart", views.get_cart, name="cart"),
	path("confirmation", views.confirmation, name="confirmation"),
]