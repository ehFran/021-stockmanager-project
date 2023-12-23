from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from stockmanager.models import Productos, Proveedores, Clientes, Compras, Ventas

###########################################################################################
################################### RUTAS STOCKMANAGE #####################################
###########################################################################################

def stockmanager_index(response):

    return render(response, 'index.html')

###########################################################################################
#################################### RUTAS PRODUCTOS ######################################
###########################################################################################

def products_index(response):

    products = Productos.objects.all()

    return render(response, 'productos/index.html', {'products': products})

def product_new(response):
    return HttpResponse('<h1>PRODUCTOS_NEW</h1>')

def product_get(response, id):
    return HttpResponse('<h1>PRODUCTOS_GET</h1>')

###########################################################################################
#################################### RUTAS PROVEEDORES ####################################
###########################################################################################

def suppliers_index(response):

    suppliers = Proveedores.objects.all()

    return render(response, 'proveedores/index.html', {'suppliers':suppliers})

def supplier_new(response):
    return HttpResponse('<h1>PROVEEDORES_NEW</h1>')

def supplier_get(response, id):
    return HttpResponse('<h1>PROVEEDORES_GET</h1>')

###########################################################################################
##################################### RUTAS CLIENTES ######################################
###########################################################################################

def clients_index(response):

    clients = Clientes.objects.all()

    return render(response, 'clientes/index.html', {'clients':clients})

def client_new(response):
    return HttpResponse('<h1>CLIENTES_NEW</h1>')

def client_get(response, id):
    return HttpResponse('<h1>CLIENTES_GET</h1>')

###########################################################################################
###################################### RUTAS COMPRAS ######################################
###########################################################################################

def purchases_index(response):

    purchases = Compras.objects.all()

    return render(response, 'compras/index.html', {'purchases':purchases})

def purchase_new(response):
    return HttpResponse('<h1>COMPRAS_NEW</h1>')

def purchase_get(response, id):
    return HttpResponse('<h1>COMPRAS_GET</h1>')

###########################################################################################
###################################### RUTAS VENTAS #######################################
###########################################################################################

def sales_index(response):

    sales = Ventas.objects.all()

    return render(response, 'ventas/index.html', {'sales':sales})

def sale_new(response):
    return HttpResponse('<h1>VENTAS_NEW</h1>')

def sale_get(response, id):
    return HttpResponse('<h1>VENTAS_GET</h1>')
