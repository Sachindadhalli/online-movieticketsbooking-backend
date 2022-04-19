from django.contrib import admin

# Register your models here.

from .models import Theatre, Movie_detail

admin.site.register(Theatre)
admin.site.register(Movie_detail)
