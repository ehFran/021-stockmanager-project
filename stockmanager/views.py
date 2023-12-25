from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from stockmanager.models import Productos, Proveedores, Clientes, Compras, Ventas
from .forms import new_product, new_supplier, new_client

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

    if response.method == 'GET':
        return render(response, 'productos/new.html', {
            'form': new_product()
        })
    else:
        Productos.objects.create(
            Nombre = response.POST['nombre'],
            Descripcion = response.POST['descripcion'],
            Precio = response.POST['precio'],
            Stock = response.POST['stock'],
            Imagen = response.FILES['imagen']
            )
        return redirect('products_index')
    

def product_get(response, ProductoID):

    product = get_object_or_404(Productos, pk=ProductoID)
    
    if response.method == 'GET':
        form = new_product(instance=product)

        return render(response, 'productos/edit.html', {
            'product': product,
            'form': form
        })
    else:
        form = new_product(response.POST, response.FILES, instance=product)
        form.save()
        return redirect('products_index')

###########################################################################################
#################################### RUTAS PROVEEDORES ####################################
###########################################################################################

def suppliers_index(response):

    suppliers = Proveedores.objects.all()

    return render(response, 'proveedores/index.html', {'suppliers':suppliers})

def supplier_new(response):
     
    if response.method == 'GET':
        return render(response, 'proveedores/new.html', {
            'form': new_supplier()
        })
    else:
        Proveedores.objects.create(
            Nombre = response.POST['nombre'],
            Contacto = response.POST['contacto'],
            CorreoElectronico = response.POST['correoelectronico'],
            Telefono = response.POST['telefono'],
            Imagen = response.FILES['imagen']
            )
        return redirect('suppliers_index')

def supplier_get(response, ProveedorID):

    supplier = get_object_or_404(Proveedores, pk=ProveedorID)
    
    if response.method == 'GET':
        form = new_supplier(instance=supplier)

        return render(response, 'proveedores/edit.html', {
            'supplier': supplier,
            'form': form
        })
    else:
        form = new_supplier(response.POST, response.FILES, instance=supplier)
        form.save()
        return redirect('suppliers_index')


###########################################################################################
##################################### RUTAS CLIENTES ######################################
###########################################################################################

def clients_index(response):

    clients = Clientes.objects.all()

    return render(response, 'clientes/index.html', {'clients':clients})

def client_new(response):
     
    if response.method == 'GET':
        return render(response, 'clientes/new.html', {
            'form': new_client()
        })
    else:
        Clientes.objects.create(
            Nombre = response.POST['nombre'],
            Apellido = response.POST['apellido'],
            CorreoElectronico = response.POST['correoelectronico'],
            Direccion = response.POST['direccion'],
            Imagen = response.FILES['imagen']
            )
        return redirect('clients_index')


def client_get(response, ClienteID):

    client = get_object_or_404(Clientes, pk=ClienteID)
    
    if response.method == 'GET':
        form = new_client(instance=client)

        return render(response, 'clientes/edit.html', {
            'client': client,
            'form': form
        })
    else:
        form = new_client(response.POST, response.FILES, instance=client)
        form.save()
        return redirect('clients_index')

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
