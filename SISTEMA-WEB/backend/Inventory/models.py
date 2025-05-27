from django.db import models

# Create your models here.
class Inventory(models.Model):
    codigo_articulo = models.IntegerField(db_column='Codigo_Articulo', blank=True, null=True)  # Field name made lowercase.
    tipo_insumo = models.CharField(db_column='Tipo_Insumo', max_length=250)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=70, blank=True, null=True)  # Field name made lowercase.
    inventario_total = models.IntegerField(db_column='Inventario_Total', blank=True, null=True)  # Field name made lowercase.
    inventario_entrega = models.IntegerField(db_column='Inventario_Entrega', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Inventory'
    