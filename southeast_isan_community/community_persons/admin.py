from django.contrib import admin

from .models import CommunityPerson


@admin.register(CommunityPerson)
class CommunityPersonAdmin(admin.ModelAdmin):
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
