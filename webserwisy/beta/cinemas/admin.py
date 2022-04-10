from django.contrib import admin

from .models import Cinema, Movie, Projection

admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(Projection)