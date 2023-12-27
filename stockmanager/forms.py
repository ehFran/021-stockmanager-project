from django import forms
from .models import Productos, Proveedores, Clientes, Compras, Ventas, DetallesCompras, DetallesVentas

#############################
###### FORMS PRODUCTOS ######
#############################

class new_product(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ['Nombre', 'Descripcion', 'Precio', 'Stock', 'Imagen']

    Nombre = forms.CharField(label='Nombre del producto:', max_length=200)
    Descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'descripcion-form'}), label="Descripción del producto:", required=False)
    Precio = forms.IntegerField(label='Precio:')
    Stock = forms.IntegerField(label='Stock:')
    Imagen = forms.ImageField(required=False)


###############################
###### FORMS PROVEEDORES ######
###############################
    
class new_supplier(forms.ModelForm):

    class Meta:
        model = Proveedores
        fields = ['Nombre', 'Contacto', 'CorreoElectronico', 'Telefono', 'Imagen']

    Nombre = forms.CharField(label='Nombre:', max_length=200)
    Contacto = forms.CharField(label='Contacto:')
    CorreoElectronico = forms.EmailField(label='Mail:')
    Telefono = forms.CharField(label='Telefono:', max_length=20)
    Imagen = forms.ImageField(required=False)
    

############################
###### FORMS CLIENTES ######
############################
    
class new_client(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ['Nombre', 'Apellido', 'Direccion', 'CorreoElectronico', 'Imagen']

    Nombre = forms.CharField(label='Nombre:', max_length=200)
    Apellido = forms.CharField(label='Apellido:', max_length=200)
    Direccion = forms.CharField(widget=forms.Textarea, label="Dirección:", required=False)
    CorreoElectronico = forms.EmailField(label='Mail:')
    Imagen = forms.ImageField(required=False)
    
    
#########################################
###### FORMS COMPRAS - PROVEEDORES ######
#########################################

class new_purchase(forms.ModelForm):

    class Meta:
        model = Compras
        fields = ['FechaCompra', 'ProveedorID']

    #Fetch Proveedores
    proveedores = Proveedores.objects.all()
    opciones_proveedores = [(proveedor.ProveedorID, proveedor.Nombre) for proveedor in proveedores]

    FechaCompra = forms.DateTimeField()
    ProveedorID = forms.ChoiceField(choices=opciones_proveedores, widget=forms.Select(attrs={'class': 'form-control'}))

#########################################
###### FORMS COMPRAS - PRODUCTOS ########
#########################################

class add_product_purchase(forms.ModelForm):

    class Meta:
        model = DetallesCompras
        fields = ['Cantidad', 'ProductoID']

    productos = Productos.objects.all()
    opciones_productos = [(producto.ProductoID, producto.Nombre) for producto in productos]

    ProductoID = forms.ChoiceField(choices=opciones_productos, widget=forms.Select(attrs={'class': 'form-product'}))
    Cantidad = forms.IntegerField(label='Cantidad')


##########################
###### FORMS VENTAS ######
##########################

class new_sale(forms.ModelForm):

    class Meta:
        model = Ventas
        fields = ['FechaVenta', 'ClienteID']

    #Fetch Clientes
    clientes = Clientes.objects.all()
    opciones_clientes= [(cliente.ClienteID, cliente.Nombre) for cliente in clientes]

    FechaVenta = forms.DateTimeField()
    ClienteID = forms.ChoiceField(choices=opciones_clientes, widget=forms.Select(attrs={'class': 'form-control'})) 


#########################################
###### FORMS COMPRAS - PRODUCTOS ########
#########################################

class add_product_sale(forms.ModelForm):

    class Meta:
        model = DetallesVentas
        fields = ['Cantidad', 'ProductoID']

    productos = Productos.objects.all()
    opciones_productos = [(producto.ProductoID, producto.Nombre) for producto in productos]

    ProductoID = forms.ChoiceField(choices=opciones_productos, widget=forms.Select(attrs={'class': 'form-product'}))
    Cantidad = forms.IntegerField(label='Cantidad')