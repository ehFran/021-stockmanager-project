from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from stockmanager.models import Productos, Proveedores, Clientes, Compras, DetallesCompras, Ventas, DetallesVentas
from .forms import new_product, new_supplier, new_client, new_purchase, add_product_purchase, new_sale, add_product_sale

###########################################################################################
################################### RUTAS STOCKMANAGE #####################################
###########################################################################################

def stockmanager_index(response):
    """
    Renderiza la página principal del gestor de inventario.

    Parameters:
    - response: Objeto de respuesta de Django.

    Returns:
    HttpResponse: Respuesta renderizada con la página principal.
    """
    return render(response, 'index.html')

###########################################################################################
#################################### RUTAS PRODUCTOS ######################################
###########################################################################################


def products_index(response):
    """
    Lista todos los productos.

    Parameters:
    - response: Objeto de respuesta de Django.

    Returns:
    HttpResponse: Respuesta renderizada con la lista de productos.
    """
    products = Productos.objects.all()

    return render(response, 'productos/index.html', {'products': products})


def product_new(response):
    """
    Crea un nuevo producto.

    Parameters:
    - response: Objeto de respuesta de Django.

    Returns:
    HttpResponse: Respuesta renderizada con el formulario de nuevo producto o redirige a la lista de productos.
    """
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
    

def product_get(response, ProductoID):
    """
    Muestra y edita un producto específico.

    Parameters:
    - response: Objeto de respuesta de Django.
    - ProductoID: ID del producto a mostrar/editar.

    Returns:
    HttpResponse: Respuesta renderizada con el formulario de edición o redirige a la lista de productos.
    """
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
    

def product_delete(response, ProductoID):
    """
    Elimina un producto específico.

    Parameters:
    - response: Objeto de respuesta de Django.
    - ProductoID: ID del producto a eliminar.

    Returns:
    HttpResponse: Redirige a la lista de productos después de la eliminación.
    """
    product = get_object_or_404(Productos, pk=ProductoID)
    
    if response.method == 'POST':
        product.delete()
        return redirect('products_index')

###########################################################################################
#################################### RUTAS PROVEEDORES ####################################
###########################################################################################


def suppliers_index(response):
    """
    Lista todos los proveedores.

    Parameters:
    - response: Objeto de respuesta de Django.

    Returns:
    HttpResponse: Respuesta renderizada con la lista de proveedores.
    """
    suppliers = Proveedores.objects.all()

    return render(response, 'proveedores/index.html', {'suppliers':suppliers})
 

def supplier_new(response):
    """
    Crea un nuevo proveedor.

    Parameters:
    - response: Objeto de respuesta de Django.

    Returns:
    HttpResponse: Respuesta renderizada con el formulario de nuevo proveedor o redirige a la lista de proveedores.
    """
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


def supplier_get(response, ProveedorID):
    """
    Muestra y edita un proveedor específico.

    Parameters:
    - response: Objeto de respuesta de Django.
    - ProveedorID: ID del proveedor a mostrar/editar.

    Returns:
    HttpResponse: Respuesta renderizada con el formulario de edición o redirige a la lista de proveedores.
    """
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


def supplier_delete(response, ProveedorID):
    """
    Elimina un proveedor específico.

    Parameters:
    - response: Objeto de respuesta de Django.
    - ProveedorID: ID del proveedor a eliminar.

    Returns:
    HttpResponse: Redirige a la lista de proveedores después de la eliminación.
    """
    supplier = get_object_or_404(Proveedores, pk=ProveedorID)
    
    if response.method == 'POST':
        supplier.delete()
        return redirect('suppliers_index')

###########################################################################################
##################################### RUTAS CLIENTES ######################################
###########################################################################################


def clients_index(response):
    """
    Lista todos los clientes.

    Parameters:
    - response: Objeto de respuesta de Django.

    Returns:
    HttpResponse: Respuesta renderizada con la lista de clientes.
    """
    clients = Clientes.objects.all()

    return render(response, 'clientes/index.html', {'clients':clients})


def client_new(response):
    """
    Crea un nuevo cliente.

    Parameters:
    - response: Objeto de respuesta de Django.

    Returns:
    HttpResponse: Respuesta renderizada con el formulario de nuevo cliente o redirige a la lista de clientes.
    """
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


def client_get(response, ClienteID):
    """
    Muestra y edita un cliente específico.

    Parameters:
    - response: Objeto de respuesta de Django.
    - ClienteID: ID del cliente a mostrar/editar.

    Returns:
    HttpResponse: Respuesta renderizada con el formulario de edición o redirige a la lista de clientes.
    """
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
    

def client_delete(response, ClienteID):
    """
    Elimina un cliente específico.

    Parameters:
    - response: Objeto de respuesta de Django.
    - ClienteID: ID del cliente a eliminar.

    Returns:
    HttpResponse: Redirige a la lista de clientes después de la eliminación.
    """
    client = get_object_or_404(Clientes, pk=ClienteID)
    
    if response.method == 'POST':
        client.delete()
        return redirect('clients_index')

###########################################################################################
###################################### RUTAS COMPRAS ######################################
###########################################################################################


def purchases_index(response):
    """
    Lista todas las compras a proveedores.

    Parameters:
    - response: Objeto de respuesta de Django.

    Returns:
    HttpResponse: Respuesta renderizada con la lista de compras a proveedores.
    """
    purchases = Compras.objects.all()

    return render(response, 'compras/index.html', {
        'purchases':purchases,
        })


def purchase_new(response):
    """
    Crea una nueva compra a proveedor.

    Parameters:
    - response: Objeto de respuesta de Django.

    Returns:
    HttpResponse: Respuesta renderizada con el formulario de nueva compra o redirige a la lista de compras.
    """
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



def purchase_get(response, CompraID):
    """
    Muestra y edita una compra a proveedor específica en detalle.

    Parameters:
    - response: Objeto de respuesta de Django.
    - CompraID: ID de la compra a proveedor a mostrar/editar.

    Returns:
    HttpResponse: Respuesta renderizada con el formulario de edición detallada o redirige a la lista de compras.
    """
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
    

def purchase_delete(response, CompraID):
    """
    Elimina una compra a proveedor específica.

    Parameters:
    - response: Objeto de respuesta de Django.
    - CompraID: ID de la compra a proveedor a eliminar.

    Returns:
    HttpResponse: Redirige a la lista de compras a proveedores después de la eliminación.
    """
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


def purchase_delete_detail(response, CompraID, DetalleCompraID):
    """
    Elimina un registro de una compra a proveedor específica.

    Parameters:
    - response: Objeto de respuesta de Django.
    - CompraID: ID de la compra a proveedor.
    - DetalleCompraID: ID del registro de detalle de compra a eliminar.

    Returns:
    HttpResponse: Redirige a la vista detallada de la compra a proveedor después de la eliminación.
    """
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


def sales_index(response):
    """
    Lista todas las ventas a clientes.

    Parameters:
    - response: Objeto de respuesta de Django.

    Returns:
    HttpResponse: Respuesta renderizada con la lista de ventas a clientes.
    """
    sales = Ventas.objects.all()

    return render(response, 'ventas/index.html', {'sales':sales})


def sale_new(response):
    """
    Crea una nueva venta.

    Parameters:
    - response: Objeto de respuesta de Django.

    Returns:
    HttpResponse: Respuesta renderizada con el formulario de nueva venta o redirige a la lista de ventas.
    """
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


def sale_get(response, VentaID):
    """
    Muestra y edita una venta concreta en detalle.

    Parameters:
    - response: Objeto de respuesta de Django.
    - VentaID: ID de la venta a mostrar/editar.

    Returns:
    HttpResponse: Respuesta renderizada con el formulario de edición detallada o redirige a la lista de ventas.
    """
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


def sale_delete(response, VentaID):
    """
    Elimina una venta concreta.

    Parameters:
    - response: Objeto de respuesta de Django.
    - VentaID: ID de la venta a eliminar.

    Returns:
    HttpResponse: Redirige a la lista de ventas después de la eliminación.
    """
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


def sale_delete_detail(response, VentaID, DetalleVentaID):
    """
    Elimina un registro de una venta concreta.

    Parameters:
    - response: Objeto de respuesta de Django.
    - VentaID: ID de la venta.
    - DetalleVentaID: ID del registro de detalle de venta a eliminar.

    Returns:
    HttpResponse: Redirige a la vista detallada de la venta después de la eliminación.
    """
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