from rest_framework import viewsets

from .models import Contacts, Node, Product
from .serializers import (
    ContactsSerializer,
    NodeReadSerializer,
    NodeUpdateSerializer,
    NodeWriteSerializer,
    ProductSerializer,
)


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

    queryset = Node.objects.all()
    # permission_classes = [IsActiveEmployee]

    def get_serializer_class(self):
        if self.action == "create":
            return NodeWriteSerializer
        elif self.action in ["update", "patch", "partial_update"]:
            return NodeUpdateSerializer
        return NodeReadSerializer

    def perform_create(self, serializer):
        serializer.save(debt=0.00)

    def perform_update(self, serializer):
        """Гарантируем, что задолженность не обновляется через API"""
        if "debt" in serializer.validated_data:
            del serializer.validated_data["debt"]
        serializer.save()
