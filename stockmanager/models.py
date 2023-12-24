from django.db import models

############################
######## PRODUCTOS #########
############################

class Productos(models.Model):
    ProductoID = models.AutoField(primary_key=True)
    Imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    Nombre = models.CharField(max_length=255)
    Descripcion = models.TextField()
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Stock = models.IntegerField()

    def __str__(self):
        return self.Nombre


###########################
######## CLIENTES #########
###########################
    
class Clientes(models.Model):
    ClienteID = models.AutoField(primary_key=True)
    Imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    Nombre = models.CharField(max_length=255)
    Apellido = models.CharField(max_length=255)
    CorreoElectronico = models.CharField(max_length=255)
    Direccion = models.TextField()

    def __str__(self):
        return self.Nombre 

############################
# VENTAS ######## CLIENTES #
############################
    
class Ventas(models.Model):
    VentaID = models.AutoField(primary_key=True)
    FechaVenta = models.DateTimeField()
    ClienteID = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    Total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "0000" + str(self.VentaID) + " - " + str(self.ClienteID.Nombre)

#############################
# VENTAS ######## PRODUCTOS #
#############################

class DetallesVentas(models.Model):
    DetalleVentaID = models.AutoField(primary_key=True)
    VentaID = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    ProductoID = models.ForeignKey(Productos, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    PrecioUnitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.DetalleVentaID) + " - " + str(self.VentaID) + " - " + self.ProductoID.Nombre

#############################
####### PROVEEDORES #########
#############################
    
class Proveedores(models.Model):
    ProveedorID = models.AutoField(primary_key=True)
    Imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    Nombre = models.CharField(max_length=255)
    Contacto = models.CharField(max_length=255)
    CorreoElectronico = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Nombre) 

################################
# COMPRAS ######## PROVEEDORES #
################################

class Compras(models.Model):
    CompraID = models.AutoField(primary_key=True)
    FechaCompra = models.DateTimeField()
    ProveedorID = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    Total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "0000" + str(self.CompraID) + " - " + str(self.ProveedorID.Nombre)

##############################
# COMPRAS ######## PRODUCTOS #
##############################
    
class DetallesCompras(models.Model):
    DetalleCompraID = models.AutoField(primary_key=True)
    CompraID = models.ForeignKey(Compras, on_delete=models.CASCADE)
    ProductoID = models.ForeignKey(Productos, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    PrecioUnitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.DetalleCompraID) + " - " + str(self.CompraID) + " - " + self.ProductoID.Nombre

##################################
# PROVEEDORES ######## PRODUCTOS #
##################################