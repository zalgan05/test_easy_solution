from django.contrib import admin
from .models import Item, Price


class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
    # list_display_links = ('name',)
    list_editable = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)
    inlines = [PriceInlineAdmin]
