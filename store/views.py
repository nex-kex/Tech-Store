from rest_framework import viewsets

from .models import Contacts, Node, Product
from .serializers import ContactsSerializer, NodeSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet класс для CRUD продуктов."""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ContactsViewSet(viewsets.ModelViewSet):
    """ViewSet класс для CRUD контактов."""

    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()


class NodeViewSet(viewsets.ModelViewSet):
    """ViewSet класс для CRUD поставщиков."""

    serializer_class = NodeSerializer
    queryset = Node.objects.all()
