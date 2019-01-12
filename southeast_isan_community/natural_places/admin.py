from django.contrib import admin

from .models import NaturalPlace


@admin.register(NaturalPlace)
class NaturalPlaceAdmin(admin.ModelAdmin):
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
