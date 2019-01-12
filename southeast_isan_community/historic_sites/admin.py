from django.contrib import admin

from .models import HistoricSite


@admin.register(HistoricSite)
class HistoricSiteAdmin(admin.ModelAdmin):
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
