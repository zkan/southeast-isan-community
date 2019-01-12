from django.contrib import admin

from .models import Career


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'community',
    )
    list_filter = (
        'community',
    )
    search_fields = (
        'name',
    )
