from django.shortcuts import render, redirect
from django.urls import reverse

from .models import ThursdayGame, FridayGame, SaturdayGame, SundayGame, MondayGame, Media, Comment

# Create your views here.
def primer(request, week):
	context = {
		"thugames": ThursdayGame.objects.filter(week=week),
		"frigames": FridayGame.objects.filter(week=week),
		"satgames": SaturdayGame.objects.filter(week=week),
		"sungames": SundayGame.objects.filter(week=week),
		"mongames": MondayGame.objects.filter(week=week),
		"media": Media.objects.filter(week=week),
		"comments": Comment.objects.filter(week=week).order_by('date'),
		"week": week
	}
	return render(request, "primer/primer.html", context)

def comment(request, week):
	name = request.POST["name"]
	comment = request.POST["comment"]
	c = Comment(name=name, comment=comment, week=week)
	c.save()

	return redirect("primer:primer", week=week)
