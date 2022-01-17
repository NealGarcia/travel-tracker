from django.contrib import admin
from .models import TripEntry, EntryDetail


# Register your models here.
admin.site.register(TripEntry)
admin.site.register(EntryDetail)