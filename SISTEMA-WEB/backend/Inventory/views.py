from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from .Serializers import InventorySerializer
from .models import Inventory
from django.db import connection
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def Create_Consult(request):
    """
    Create a new inventory item or retrieve all items.
    """
    if request.method == 'POST':
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'GET':
        try:
            inventory_items = Inventory.objects.all()
            serializer = InventorySerializer(inventory_items, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def Inventory_Total(request):
    if request.method == 'GET':
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT Tipo_Insumo, Inventario_Total, Inventario_Entrega FROM Inventory')
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]
                resultado = [dict(zip(columns, row)) for row in rows]
            return Response(resultado)
        except Exception as e:
            return Response({'error': str(e)}, status=500)