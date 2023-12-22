from django.contrib import admin
from .models import Productos, Proveedores, Clientes, Ventas, Compras, DetallesCompras, DetallesVentas

################################
##### MODELOS STOCKMANAGER #####
################################

admin.site.register(Productos)
admin.site.register(Proveedores)
admin.site.register(Clientes)
admin.site.register(Ventas)
admin.site.register(DetallesVentas)
admin.site.register(Compras)
admin.site.register(DetallesCompras)


