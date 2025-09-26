from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Класс для пользователей системы."""

    email = models.EmailField(unique=True, blank=True, null=True, verbose_name="Email")
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Имя")
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Фамилия")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
