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

## DIA 1:
  - Creación del projecto [smartstorage] y el repositorio.
  - Creación apps [stockmanager] Añadidas a INSTALLED_APPS.
  - Migraciones realizadas y super user creado [name: fran, pw:fran]
  - Creación de ruta maestra [stockmanager] y urls.py 
  - Estructura stockmanager.views creada. Clases definidas.
  - Urlpatterns definido.

