from django.contrib import admin

from .models import Deed


@admin.register(Deed)
class DeedAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'talent',
        'points',
        'times_completed',
    )
    fields = (
        'title',
        'user',
        'talent',
        'points',
        'description',
        'times_completed',
    )
    search_fields = (
        'title',
        'description',
    )
