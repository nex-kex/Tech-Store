from django.contrib import admin

from .models import Contacts, Node, Product


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["email", "country", "city", "street"]
    list_filter = ["country", "city"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "model", "release_date"]
    list_filter = ["release_date"]


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "debt", "created_at"]
    list_filter = ["level"]
