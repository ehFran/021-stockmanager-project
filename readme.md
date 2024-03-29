```python
-------------------------------------------------------------------------
  |--- VISTAS
        |
        |
        |--- INDEX (EXPLICACION DEL PRODUCTO: SMART STORAGE)
          |
          |- STOCK MANAGER
            |---> CLIENTS_INDEX (LISTADO [+UPDATE, +DELETE]), CLIENT_NEW (CREATE), CLIENT_GET(ID)     
            |---> SUPPLIERS_INDEX (LISTADO [+UPDATE, +DELETE]), SUPPLIER_NEW (CREATE), SUPPLIER_GET(ID)
            |---> PRODUCTS_INDEX (LISTADO [+UPDATE, +DELETE]), PRODUCT_NEW (CREATE), PRODUCT_GET (ID)
            |---> SALES_INDEX (LISTADO [+UPDATE, +DELETE]), SALE_NEW (CREATE), SALE_GET(ID)
            |---> PURCHASES_INDEX (LISTADO [+UPDATE, +DELETE]), PURCHASE_NEW (CREATE), PURCHASE_GET(ID)
        |
        **************************
        |
        |--- DASHBOARDS
                |- VENTAS
                |- COMPRAS
                |- PREDICCION VENTAS 
                |- PREDICCION STOCK - GESTION DE PEDIDOS A PROVEEDORES (MAIL) 
                |- MAILING CON PROMOCIONES A CLIENTES

---------------------------------------------------------------------------
```

## DIA 1:
  - Creación del projecto [smartstorage] y el repositorio
  - Creación apps [stockmanager] Añadidas a INSTALLED_APPS
  - Migraciones realizadas y super user creado [name: fran, pw:fran]
  - Creación de ruta maestra [stockmanager] y urls.py 
  - Estructura stockmanager.views creada. Clases definidas
  - Urlpatterns definido

## DIA 2:
  - Modelos base de datos creados. [Falta uno para relacionar proveedores y productos]
  - Modelos añadidos a administración
  - Estructura static y templates

## DIA 3:
  - Instalación tailwind. Creación theme. [run server tailwind => python manage.py tailwind start]
  - DaisyUI instalado y añadido a tailwind config
  - NavBar e indexado de Productos, Proveedores, Clientes, Compras y Ventas

## DIA 4:
  - Creados primeros formularios (New: Productos, Proveedores y Clientes)
  - Funciones new_product, new_supplier, new_client
  - Sistema de gestión de imagenes create para productos, proveedores y clientes. Instalación pillow. Modelos modificados y migrados

## DIA 5:
  - Funciones y vistas de edición (edit.html) productos, proveedores y clientes
  - Sistema de visionado de Compras: index y details

## DIA 6:
  - Sistema de visionado de Ventas: index y details.
  - Creación de compras y detalles compras. Actualización total funcionando
  - Creación de ventas y detalles de ventas. Actualización de total funcionando

## DIA 7:
  - Estilado básico
  - Index main

## DIA 8:
  - Eliminar productos, proveedores y clientes
  - Eliminar lineas de registros en ventas y compras
  - Actualizar el stock de los productos conforme se generen nuevas compras y ventas. O se modifiquen los registros de estas
  - Docstrings generados para views y urls



  