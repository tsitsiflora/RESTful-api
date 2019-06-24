from django.contrib import admin
from .models import Movies, Directors, Actors
# Register your models here.


admin.site.register(Movies)
admin.site.register(Directors)
admin.site.register(Actors)

