from django.contrib import admin

from lunchMenu.models import LunchMenu


# Register your models here.

@admin.register(LunchMenu)
class LunchMenuAdmin(admin.ModelAdmin):
     pass