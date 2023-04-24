from django.contrib import admin

from .models import Talent


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'title',
    )
    fields = (
        'title',
        'user',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
