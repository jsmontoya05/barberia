from django.db import models

# Create your models here.

class Usuario (models.Model):

    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False, blank=False)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    password = models.CharField(max_length=20, null=False, blank=False)
    celular = models.CharField(max_length=15)
    rol_choises = (
        ('1', 'Administrador'),
        ('2', 'Barbero'),
        ('3', 'Cliente')
    )
    rol = models.CharField(max_length=1, choices=rol_choises, default='3')

    def __str__(self):
        return self.nombre


class Barbero(models.Model):

    id_barbero = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    detalle = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='app')

    def __str__(self):
        return str(self.id_usuario)


class Catalogo(models.Model):

    id_catalogo = models.AutoField(primary_key=True)
    tipo_choices = (
        ('0', 'Servicio'),
        ('1', 'Producto')
    )
    tipo = models.CharField(max_length=1, choices=tipo_choices, default='0')
    nombre = models.CharField(max_length=30,null=False, blank=False)
    detalle = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False, default=0)
    imagen = models.ImageField(upload_to='app')

    def __str__(self):
        return self.nombre


class Hora(models.Model):

    id_hora = models.AutoField(primary_key=True)
    hora = models.TimeField(blank=False, null=False)

    def __str__(self):
        return str(self.hora)


class Reserva(models.Model):

    id_reserva = models.AutoField(primary_key=True)
    fecha = models.DateField(null=False, blank=False)
    id_hora = models.ForeignKey(Hora, null=False, blank=False, on_delete=models.DO_NOTHING)
    id_usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.DO_NOTHING)
    id_barbero = models.ForeignKey(Barbero, null=False, blank=False, on_delete=models.DO_NOTHING)
    id_catalogo = models.ForeignKey(Catalogo, null=False, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.fecha)
