from django.urls import path
from . import views

# Create your views here.
app_name = "primer"
urlpatterns = [
	path("<int:week>", views.primer, name="primer"),
	path("<int:week>/comment", views.comment, name="comment")
]