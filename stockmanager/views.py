from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse

###########################################################################################
################################### RUTAS STOCKMANAGE #####################################
###########################################################################################

def stockmanager_index(response):
    return HttpResponse('<h1>INDEX DE STOCK MANAGER</h1>')

###########################################################################################
#################################### RUTAS PRODUCTOS ######################################
###########################################################################################

def products_index(response):
    return HttpResponse('<h1>PRODUCTOS_INDEX</h1>')

def product_new(response):
    return HttpResponse('<h1>PRODUCTOS_NEW</h1>')

def product_get(response, id):
    return HttpResponse('<h1>PRODUCTOS_GET</h1>')

###########################################################################################
#################################### RUTAS PROVEEDORES ####################################
###########################################################################################

def suppliers_index(response):
    return HttpResponse('<h1>PROVEEDORES_INDEX</h1>')

def supplier_new(response):
    return HttpResponse('<h1>PROVEEDORES_NEW</h1>')

def supplier_get(response, id):
    return HttpResponse('<h1>PROVEEDORES_GET</h1>')

###########################################################################################
##################################### RUTAS CLIENTES ######################################
###########################################################################################

def clients_index(response):
    return HttpResponse('<h1>CLIENTES_INDEX</h1>')

def client_new(response):
    return HttpResponse('<h1>CLIENTES_NEW</h1>')

def client_get(response, id):
    return HttpResponse('<h1>CLIENTES_GET</h1>')

###########################################################################################
###################################### RUTAS COMPRAS ######################################
###########################################################################################

def purchases_index(response):
    return HttpResponse('<h1>COMPRAS_INDEX</h1>')

def purchase_new(response):
    return HttpResponse('<h1>COMPRAS_NEW</h1>')

def purchase_get(response, id):
    return HttpResponse('<h1>COMPRAS_GET</h1>')

###########################################################################################
###################################### RUTAS VENTAS #######################################
###########################################################################################

def sales_index(response):
    return HttpResponse('<h1>VENTAS_INDEX</h1>')

def sale_new(response):
    return HttpResponse('<h1>VENTAS_NEW</h1>')

def sale_get(response, id):
    return HttpResponse('<h1>VENTAS_GET</h1>')
