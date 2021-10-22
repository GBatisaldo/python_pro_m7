from django.contrib import admin
from .models import FavMovie, ProjetoDjango

# Register your models here.

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('movie_title','image_tag')

admin.site.register(ProjetoDjango)
admin.site.register(FavMovie)