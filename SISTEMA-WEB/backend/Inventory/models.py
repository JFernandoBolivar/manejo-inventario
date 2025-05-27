from django.db import models
from django.utils import timezone

# Create your models here.
class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_articulo = models.CharField(db_column='Codigo_Articulo', max_length=50, default='N/A')
   
    tipo_insumo = models.CharField(db_column='Tipo_Insumo', max_length=250, default='No especificado')
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)
    estado = models.CharField(db_column='Estado', max_length=50, default='Disponible')
    numero_factura = models.CharField(db_column='Numero_Factura', max_length=50, blank=True, null=True)
    inventario_total = models.IntegerField(db_column='Inventario_Total', default=0)
    inventario_entrega = models.IntegerField(db_column='Inventario_Entrega', default=0)
    fecha_adquisicion = models.DateField(db_column='Fecha_Adquisicion', default=timezone.now)
    fecha_mantenimiento = models.DateField(db_column='Fecha_Mantenimiento', blank=True, null=True)
    
   
    categoria = models.CharField(db_column='Categoria', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Inventory'
    
    def __str__(self):
        return f"{self.codigo_articulo} - {self.nombre}"
