from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from apps.city.models import Citizen, Job


@admin.register(Citizen)
class CitizenAdmin(UserAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo_preview']

    def photo_preview(self, obj):
        return format_html('<img src="{}" width="75px" />'.format(obj.photo.url))

    photo_preview.short_description = 'Photo Preview'
