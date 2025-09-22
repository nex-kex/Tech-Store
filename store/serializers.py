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


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        exclude = ["created_at"]
