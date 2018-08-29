from django.db import models

# Create your models here.
class ThursdayGame(models.Model):
	week = models.IntegerField()
	team1 = models.CharField(max_length=64)
	team1image = models.CharField(max_length=64)
	team2 = models.CharField(max_length=64)
	team2image = models.CharField(max_length=64)
	time = models.CharField(max_length=64)
	network_image = models.CharField(max_length=64)

class FridayGame(models.Model):
	week = models.IntegerField()
	team1 = models.CharField(max_length=64)
	team1image = models.CharField(max_length=64)	
	team2 = models.CharField(max_length=64)
	team2image = models.CharField(max_length=64)	
	time = models.CharField(max_length=64)
	network_image = models.CharField(max_length=64)	

class SaturdayGame(models.Model):
	week = models.IntegerField()
	team1 = models.CharField(max_length=64)
	team1image = models.CharField(max_length=64)	
	team2 = models.CharField(max_length=64)
	team2image = models.CharField(max_length=64)	
	time = models.CharField(max_length=64)
	network_image = models.CharField(max_length=64)	

class SundayGame(models.Model):
	week = models.IntegerField()
	team1 = models.CharField(max_length=64)
	team1image = models.CharField(max_length=64)	
	team2 = models.CharField(max_length=64)
	team2image = models.CharField(max_length=64)	
	time = models.CharField(max_length=64)
	network_image = models.CharField(max_length=64)	

class MondayGame(models.Model):
	week = models.IntegerField()
	team1 = models.CharField(max_length=64)
	team1image = models.CharField(max_length=64)	
	team2 = models.CharField(max_length=64)
	team2image = models.CharField(max_length=64)	
	time = models.CharField(max_length=64)
	network_image = models.CharField(max_length=64)

class Media(models.Model):
	week = models.IntegerField()
	title = models.CharField(max_length=64)	
	entry_image = models.CharField(max_length=64, blank=True)	
	entry = models.TextField()
	hottake = models.TextField()

class Comment(models.Model):
	name = models.CharField(max_length=64)
	comment = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	week = models.IntegerField()