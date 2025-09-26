from django.contrib import admin, messages

from .models import Contacts, Node, Product


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "country", "city", "street"]
    list_filter = ["country", "city"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "model", "release_date"]
    list_filter = ["release_date"]


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "level", "debt", "contacts__city"]
    list_filter = ["level", "contacts__city"]
    actions = ["clear_debt_action"]

    def clear_debt_action(self, request, queryset):
        """Admin action для очистки задолженности у выбранных поставщиков"""
        suppliers_with_debt = queryset.filter(debt__gt=0)
        count = suppliers_with_debt.count()

        if count == 0:
            self.message_user(request, "У выбранных поставщиков нет задолженности", messages.WARNING)
            return

        updated_count = suppliers_with_debt.update(debt=0.00)

        if updated_count == 1:
            message = "Задолженность очищена для 1 поставщика"
        else:
            message = f"Задолженность очищена для {updated_count} поставщиков"

        self.message_user(request, message, messages.SUCCESS)

    clear_debt_action.short_description = "Очистить задолженность у выбранных поставщиков"
