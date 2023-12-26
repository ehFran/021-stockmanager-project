from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from stockmanager.models import Productos, Proveedores, Clientes, Compras, DetallesCompras, Ventas, DetallesVentas
from .forms import new_product, new_supplier, new_client

###########################################################################################
################################### RUTAS STOCKMANAGE #####################################
###########################################################################################

def stockmanager_index(response):

    return render(response, 'index.html')

###########################################################################################
#################################### RUTAS PRODUCTOS ######################################
###########################################################################################

''' LISTAR TODOS LOS PRODUCTOS '''
def products_index(response):

    products = Productos.objects.all()

    return render(response, 'productos/index.html', {'products': products})

''' CREAR UN NUEVO PRODUCTO '''
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
    
''' VER Y EDITAR UN PRODUCTO CONCRETO'''
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

''' LISTAR TODOS LOS PROVEEDORES '''
def suppliers_index(response):

    suppliers = Proveedores.objects.all()

    return render(response, 'proveedores/index.html', {'suppliers':suppliers})

''' CREAR UN NUEVO PROVEEDOR '''
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

''' VER Y EDITAR UN PROVEEDOR CONCRETO '''
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

''' LISTAR TODOS LOS CLIENTES '''
def clients_index(response):

    clients = Clientes.objects.all()

    return render(response, 'clientes/index.html', {'clients':clients})


''' CREAR UN NUEVO CLIENTE '''
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

''' VER Y EDITAR UN CLIENTE CONCRETO '''
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

''' LISTAR TODAS LAS COMPRAS A PROVEEDORES '''
def purchases_index(response):

    purchases = Compras.objects.all()

    return render(response, 'compras/index.html', {
        'purchases':purchases,
        })

''' CREAR UNA NUEVA COMPRA A PROVEEDOR '''
def purchase_new(response):
    return HttpResponse('<h1>COMPRAS_NEW</h1>')

''' EDITAR UNA COMPRA CONCRETA A PROVEEDOR '''
def purchase_edit(response):
    pass

''' VER UNA COMPRA CONCRETA EN DETALLE '''
def purchase_get(response, CompraID):

    purchase = Compras.objects.get(pk=CompraID)
    purchase_details = DetallesCompras.objects.filter(CompraID=CompraID)

    return render(response, 'compras/detail.html', {
        'purchase': purchase,
        'purchase_details': purchase_details,
    })

###########################################################################################
###################################### RUTAS VENTAS #######################################
###########################################################################################

''' LISTAR TODAS LAS VENTAS A CLIENTES '''
def sales_index(response):

    sales = Ventas.objects.all()

    return render(response, 'ventas/index.html', {'sales':sales})


''' CREAR NUEVA VENTA '''
def sale_new(response):
    return HttpResponse('<h1>VENTAS_NEW</h1>')


''' EDITAR UNA VENTA CONCRETA A UN CLIENTE  '''
def sale_update(response):
    pass

''' VER UNA VENTA CONCRETA EN DETALLE '''
def sale_get(response, VentaID):

    sale = Ventas.objects.get(pk=VentaID)
    sale_details = DetallesVentas.objects.filter(VentaID=VentaID)

    return render(response, 'ventas/detail.html', {
        'sale': sale,
        'sale_details': sale_details,
    })
