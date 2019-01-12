from django.contrib import admin

from .models import HistoricalSite


@admin.register(HistoricalSite)
class HistoricalSiteAdmin(admin.ModelAdmin):
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
