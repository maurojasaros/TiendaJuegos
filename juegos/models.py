from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Modelos principales
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']  # Ordenar categorías por nombre
        db_table = 'categorias'  # Nombre de la tabla en la base de datos

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='juegos')

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']  # Ordenar juegos por nombre
        db_table = 'juegos'  # Nombre de la tabla en la base de datos

class TipoUsuario(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'tipo_usuarios'  # Nombre de la tabla en la base de datos

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.TextField()
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'perfiles_usuarios'  # Nombre de la tabla en la base de datos

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

    class Meta:
        db_table = 'carritos'  # Nombre de la tabla en la base de datos

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def subtotal(self):
        return self.juego.precio * self.cantidad  # Método para calcular el subtotal

    def __str__(self):
        return f"{self.cantidad} x {self.juego.nombre} en carrito"

    class Meta:
        db_table = 'ITEMS_CARRITO'  # Nombre de la tabla en la base de datos

class Pedido(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido realizado el {self.fecha_pedido}"

    class Meta:
        db_table = 'pedidos'  # Nombre de la tabla en la base de datos

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)