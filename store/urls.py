from django.urls import path

from . import views
from .apps import StoreConfig

app_name = StoreConfig.name

urlpatterns = []
