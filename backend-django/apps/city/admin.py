from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.city.models import Citizen, Job


@admin.register(Citizen)
class CitizenAdmin(UserAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass
