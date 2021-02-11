from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Films)
admin.site.register(models.Actors)
# admin.site.register(models.FilmsCountries)
# admin.site.register(models.FilmsDirectors)
# admin.site.register(models.FilmsActors)
admin.site.register(models.Types)
admin.site.register(models.Genres)
admin.site.register(models.Countries)
admin.site.register(models.Years)