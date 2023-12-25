from django.urls import path
from . import views

urlpatterns = [

    #STOCKMANAGER INDEX
    path('', views.stockmanager_index, name='stockmanager_index'),

    #PRODUCTOS = PRODUCTS
    path('productos/', views.products_index, name='products_index'),
    path('producto_nuevo/', views.product_new, name='product_new'),
    path('producto/<int:ProductoID>', views.product_get, name='product_get'),
     
    #PROVEEDORES = SUPPLIERS
    path('proveedores/', views.suppliers_index, name='suppliers_index'),
    path('proveedor_nuevo/', views.supplier_new, name='supplier_new'),
    path('proveedor/<int:ProveedorID>', views.supplier_get, name='supplier_get'),
     
    #CLIENTES = CLIENTS
    path('clientes/', views.clients_index, name='clients_index'),
    path('cliente_nuevo/', views.client_new, name='client_new'),
    path('cliente/<int:ClienteID>', views.client_get, name='client_get'),
     
    #COMPRAS = PURCHASES
    path('compras/', views.purchases_index, name='purchases_index'),
    path('compra_nueva/', views.purchase_new, name='purchase_new'),
    path('compra/<int:id>', views.purchase_get, name='purchase_get'),
     
    #VENTAS = SALES
    path('ventas/', views.sales_index, name='sales_index'),
    path('venta_nueva/', views.sale_new, name='sale_new'),
    path('venta/<int:id>', views.sale_get, name='sale_get'),
]