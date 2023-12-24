from django import forms
from .models import Proveedores, Clientes

#############################
###### FORMS PRODUCTOS ######
#############################

class new_product(forms.Form):

    nombre = forms.CharField(label='Nombre del producto:', max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripción del producto:", required=False)
    precio = forms.IntegerField(label='Precio:')
    stock = forms.IntegerField(label='Stock:')
    imagen = forms.ImageField(required=False)


###############################
###### FORMS PROVEEDORES ######
###############################
    
class new_supplier(forms.Form):

    nombre = forms.CharField(label='Nombre:', max_length=200)
    contacto = forms.CharField(label='Contacto:')
    correoelectronico = forms.EmailField(label='Mail:')
    telefono = forms.CharField(label='Telefono:', max_length=20)
    imagen = forms.ImageField(required=False)
    

############################
###### FORMS CLIENTES ######
############################
    
class new_client(forms.Form):

    nombre = forms.CharField(label='Nombre:', max_length=200)
    apellido = forms.CharField(label='Apellido:', max_length=200)
    direccion = forms.CharField(widget=forms.Textarea, label="Dirección:", required=False)
    correoelectronico = forms.EmailField(label='Mail:')
    imagen = forms.ImageField(required=False)
    
    
###########################
###### FORMS COMPRAS ######
###########################

class new_purchase(forms.Form):

    #Fetch Proveedores
    proveedores = Proveedores.objects.all()
    opciones_proveedores = [(proveedor.ProveedorID, proveedor.Nombre) for proveedor in proveedores]

    fechacompra = forms.DateTimeField()
    proveedor = forms.ChoiceField(choices=opciones_proveedores, widget=forms.Select(attrs={'class': 'form-control'}))



##########################
###### FORMS VENTAS ######
##########################

