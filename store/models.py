from datetime import datetime

from django.db import models


class Product(models.Model):
    """Класс для описания продуктов"""

    name = models.CharField(max_length=50, verbose_name="Название")
    model = models.CharField(max_length=50, verbose_name="Модель")
    release_date = models.DateTimeField(default=datetime.now(), verbose_name="Дата выхода продукта на рынок")

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["release_date"]


class Contacts(models.Model):
    """Класс для описания контактов одного звена сети"""

    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=20, verbose_name="Страна")
    city = models.CharField(max_length=20, verbose_name="Город")
    street = models.CharField(max_length=30, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Node(models.Model):
    """Класс для описания модели звена сети"""

    name = models.CharField(max_length=50, verbose_name="Название")
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name="Контакты")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    level = models.IntegerField(verbose_name="Уровень иерархии")
    supplier = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", verbose_name="Поставщик")
    debt = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Задолженность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def save(self, *args, **kwargs):
        """Определение уровня иерархии"""
        if self.supplier is None:
            self.level = 0
        else:
            self.level = self.supplier.level + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ["created_at"]
