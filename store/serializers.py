from rest_framework import serializers

from .models import Contacts, Node, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"


class NodeReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения данных поставщика"""

    contacts = ContactsSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Node
        fields = "__all__"
        read_only_fields = ["debt", "created_at"]


class NodeWriteSerializer(serializers.ModelSerializer):
    """Сериализатор для создания/обновления поставщика"""

    class Meta:
        model = Node
        exclude = ["debt", "created_at", "level"]


class NodeUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор специально для обновления (без поля debt)"""

    class Meta:
        model = Node
        read_only_fields = ["debt", "created_at", "level"]
