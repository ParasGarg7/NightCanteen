from django.contrib import admin
from .models import Item

class ItemModelAdmin(admin.ModelAdmin):
    list_display = ["title","price","quantity","i_type"]
    list_display_links=["title"]
    list_filter=["price"]
    search_fields=["title"]
    list_editable = ["quantity"]

admin.site.register(Item,ItemModelAdmin)