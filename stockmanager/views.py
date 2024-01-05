from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from stockmanager.models import Productos, Proveedores, Clientes, Compras, DetallesCompras, Ventas, DetallesVentas
from .forms import new_product, new_supplier, new_client, new_purchase, add_product_purchase, new_sale, add_product_sale

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
            Nombre = response.POST['Nombre'],
            Descripcion = response.POST['Descripcion'],
            Precio = response.POST['Precio'],
            Stock = response.POST['Stock'],
            Imagen = response.FILES['Imagen']
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
    
''' ELIMINAR UN PRODUCTO CONCRETO'''
def product_delete(response, ProductoID):

    product = get_object_or_404(Productos, pk=ProductoID)
    
    if response.method == 'POST':
        product.delete()
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
            Nombre = response.POST['Nombre'],
            Contacto = response.POST['Contacto'],
            CorreoElectronico = response.POST['CorreoElectronico'],
            Telefono = response.POST['Telefono'],
            Imagen = response.FILES['Imagen']
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

''' ELIMINAR UN PROVEEDOR CONCRETO'''
def supplier_delete(response, ProveedorID):

    supplier = get_object_or_404(Proveedores, pk=ProveedorID)
    
    if response.method == 'POST':
        supplier.delete()
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
            Nombre = response.POST['Nombre'],
            Apellido = response.POST['Apellido'],
            CorreoElectronico = response.POST['CorreoElectronico'],
            Direccion = response.POST['Direccion'],
            Imagen = response.FILES['Imagen']
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
    
''' ELIMINAR UN CLIENTE CONCRETO'''
def client_delete(response, ClienteID):

    client = get_object_or_404(Clientes, pk=ClienteID)
    
    if response.method == 'POST':
        client.delete()
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
     
    if response.method == 'GET':
        return render(response, 'compras/new.html', {
            'form': new_purchase()
        })
    else:
         # Obtén la instancia del proveedor usando el ID del formulario
        proveedor_id = response.POST['ProveedorID']
        proveedor = Proveedores.objects.get(ProveedorID=proveedor_id)

        # Crea la nueva compra utilizando la instancia del proveedor
        Compras.objects.create(
            FechaCompra=response.POST['FechaCompra'],
            ProveedorID=proveedor,
            Total=0,
            )
        
        return redirect('purchases_index')


''' EDITAR UNA COMPRA CONCRETA A PROVEEDOR '''
def purchase_edit(response):
    pass

''' VER Y EDITAR UNA COMPRA CONCRETA EN DETALLE '''
def purchase_get(response, CompraID):

    purchase = Compras.objects.get(pk=CompraID)
    purchase_details = DetallesCompras.objects.filter(CompraID=CompraID)

    if response.method == 'GET':
        return render(response, 'compras/detail.html', {
            'form': add_product_purchase(),
            'purchase': purchase,
            'purchase_details': purchase_details,
        })
    else:
        # Obtén la instancia del producto usando el ID del formulario
        producto_id = response.POST['ProductoID']
        producto = Productos.objects.get(ProductoID=producto_id)

        # Crea nuevo detalle utilizando la instancia de compra y producto
        DetallesCompras.objects.create(
            Cantidad=response.POST['Cantidad'],
            CompraID=purchase,
            ProductoID=producto,
            PrecioUnitario=producto.Precio
            )
        purchase.Total = float(purchase.Total) + (float(producto.Precio) * int(response.POST['Cantidad']))
        producto.Stock = producto.Stock + int(response.POST['Cantidad'])
        producto.save()
        purchase.save()
        
        return redirect('purchase_get', CompraID)
    
''' ELIMINAR UNA COMPRA CONCRETA'''
def purchase_delete(response, CompraID):

    purchase = get_object_or_404(Compras, pk=CompraID)
    
    if response.method == 'POST':

        detalles_compras = DetallesCompras.objects.filter(CompraID=CompraID)

        # Actualiza el stock de los productos asociados a cada detalle de compra
        for detalle_compra in detalles_compras:
            producto = detalle_compra.ProductoID
            cantidad = detalle_compra.Cantidad

            # Ajusta el stock del producto restando la cantidad de la compra
            producto.Stock -= cantidad
            producto.save()
        
        purchase.delete()
        return redirect('purchases_index')

''' ELIMINAR UN REGISTRO DE UNA COMPRA'''
def purchase_delete_detail(response, CompraID, DetalleCompraID):

    purchase_register = get_object_or_404(DetallesCompras, pk=DetalleCompraID)
    purchase = get_object_or_404(Compras, pk=CompraID)
    
    if response.method == 'POST':
        purchase.Total = purchase.Total - (purchase_register.Cantidad * purchase_register.PrecioUnitario)
        producto = get_object_or_404(Productos, pk=purchase_register.ProductoID.ProductoID)
        producto.Stock -= purchase_register.Cantidad
        producto.save()
        purchase.save()
        purchase_register.delete()
        return redirect('purchase_get', CompraID=CompraID)

###########################################################################################
###################################### RUTAS VENTAS #######################################
###########################################################################################

''' LISTAR TODAS LAS VENTAS A CLIENTES '''
def sales_index(response):

    sales = Ventas.objects.all()

    return render(response, 'ventas/index.html', {'sales':sales})


''' CREAR NUEVA VENTA '''
def sale_new(response):

    if response.method == 'GET':
        return render(response, 'ventas/new.html', {
            'form': new_sale()
        })
    else:
        cliente_id = response.POST['ClienteID']
        cliente = Clientes.objects.get(ClienteID=cliente_id)

        Ventas.objects.create(
            FechaVenta=response.POST['FechaVenta'],
            ClienteID=cliente,
            Total=0
        )

        return redirect('sales_index')


''' EDITAR UNA VENTA CONCRETA A UN CLIENTE  '''
def sale_update(response):
    pass

''' VER UNA VENTA CONCRETA EN DETALLE '''
def sale_get(response, VentaID):

    sale = Ventas.objects.get(pk=VentaID)
    sale_details = DetallesVentas.objects.filter(VentaID=VentaID)

    if response.method == 'GET':
        return render(response, 'ventas/detail.html', {
            'form': add_product_sale(),
            'sale': sale,
            'sale_details': sale_details,
        })
    else:
        # Obtén la instancia del producto usando el ID del formulario
        producto_id = response.POST['ProductoID']
        producto = Productos.objects.get(ProductoID=producto_id)

        # Crea nuevo detalle utilizando la instancia de venta y producto
        DetallesVentas.objects.create(
            Cantidad=response.POST['Cantidad'],
            VentaID=sale,
            ProductoID=producto,
            PrecioUnitario=producto.Precio
            )
        
        sale.Total = float(sale.Total) + (float(producto.Precio) * int(response.POST['Cantidad']))
        producto.Stock = producto.Stock - int(response.POST['Cantidad'])
        producto.save()
        sale.save()
        
        return redirect('sale_get', VentaID)

''' ELIMINAR UNA VENTA'''
def sale_delete(response, VentaID):

    sale = get_object_or_404(Ventas, pk=VentaID)
    
    if response.method == 'POST':

        detalles_ventas = DetallesVentas.objects.filter(VentaID=VentaID)

        # Actualiza el stock de los productos asociados a cada detalle de compra
        for detalle_venta in detalles_ventas:
            producto = detalle_venta.ProductoID
            cantidad = detalle_venta.Cantidad

            # Ajusta el stock del producto restando la cantidad de la compra
            producto.Stock += cantidad
            producto.save()

        sale.delete()
        return redirect('sales_index')

''' ELIMINAR UN REGISTRO DE UNA VENTA'''
def sale_delete_detail(response, VentaID, DetalleVentaID):

    sale_register = get_object_or_404(DetallesVentas, pk=DetalleVentaID)
    sale = get_object_or_404(Ventas, pk=VentaID)
    
    if response.method == 'POST':
        sale.Total = sale.Total - (sale_register.Cantidad * sale_register.PrecioUnitario)
        sale.save()
        producto = get_object_or_404(Productos, pk=sale_register.ProductoID.ProductoID)
        producto.Stock += sale_register.Cantidad
        producto.save()
        sale_register.delete()
        return redirect('sale_get', VentaID=VentaID)