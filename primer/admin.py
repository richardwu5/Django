from django.contrib import admin

from .models import FridayGame, SaturdayGame, SundayGame, MondayGame, Media, Comment

# Register your models here.
admin.site.register(FridayGame)
admin.site.register(SaturdayGame)
admin.site.register(SundayGame)
admin.site.register(MondayGame)
admin.site.register(Media)
admin.site.register(Comment)