from django.contrib import admin

from .models import CommunityPerson


@admin.register(CommunityPerson)
class CommunityPersonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'role',
        'community',
    )
    list_filter = (
        'role',
        'community',
    )
    search_fields = (
        'name',
    )
