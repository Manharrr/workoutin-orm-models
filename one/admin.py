from django.contrib import admin

# Register your models here.

from .models import Theater,Movie

admin.site.register(Movie)
admin.site.register(Theater)