from django.urls import path
from . import views

# Create your views here.
app_name = "pizza"
urlpatterns = [
	path("", views.pizza, name="pizza"),
	path("login", views.login_view, name="login"),
	path("logout", views.logout_view, name="logout")	
]