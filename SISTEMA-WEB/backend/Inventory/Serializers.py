from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
        read_only_fields = ['id']  # Proteger el campo id para que no se pueda modificar