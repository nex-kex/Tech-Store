# from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .apps import StoreConfig

app_name = StoreConfig.name

router = DefaultRouter()
router.register(r"products", views.ProductViewSet, basename="products")
router.register(r"contacts", views.ContactsViewSet, basename="contacts")
router.register(r"suppliers", views.NodeViewSet, basename="suppliers")

urlpatterns = [] + router.urls
