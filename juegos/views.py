from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import RegistroForm
from .forms import JuegoForm 
from .models import Juego, Carrito, ItemCarrito, Pedido
from django.contrib.auth.views import LoginView

# Vista principal de la aplicación, solo accesible para usuarios autenticados
@login_required
def index(request):
    context = {
        'is_superuser': request.user.is_superuser, # Determina si el usuario es superusuario
    }
    return render(request,'juegos/index.html', context)


def formulario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('nombre_usuario')
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Crear el usuario en la base de datos
            user = User.objects.create_user(
                username=nombre_usuario,
                first_name=nombre,
                last_name=apellido,
                email=email,
                password=password
            )

            # Crear un carrito para el usuario recién registrado
            Carrito.objects.create(usuario=user)

            # Iniciar sesión automáticamente después del registro
            login(request, user)

            messages.success(request, 'Registro completado con éxito. Has iniciado sesión automáticamente.')
            return redirect('index')  # Redirige a la página principal o a donde desees
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = RegistroForm()  # Si es una petición GET, crea un formulario vacío

    return render(request, 'juegos/formulario.html', {'form': form})


# Vistas para las categorías de juegos
def aventuras(request):
    return render(request, 'juegos/aventuras.html')

def deportes(request):
    return render(request, 'juegos/deportes.html')

def rpg(request):
    return render(request, 'juegos/rpg.html')

def shooter(request):
    return render(request, 'juegos/shooter.html')

def terror(request):
    return render(request, 'juegos/terror.html')

def inicio_sesion(request):
    return render(request, 'juegos/inicio_sesion.html')

# Listar juegos
@login_required       
def listar_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos/listar_juegos.html', {'juegos': juegos})

# Ver detalles de un juego
def ver_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    return render(request, 'juegos/ver_juego.html', {'juego': juego})

# Crear un nuevo juego
@login_required       
def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_juegos')
    else:
        form = JuegoForm()
    return render(request, 'juegos/crear_juego.html', {'form': form})

# Editar un juego existente
@login_required       
def editar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('ver_juego', pk=juego.pk)
    else:
        form = JuegoForm(instance=juego)
    return render(request, 'juegos/editar_juego.html', {'juego': juego, 'form': form})

# Eliminar un juego
@login_required       
def eliminar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        juego.delete()
        return redirect('listar_juegos')
    return render(request, 'juegos/eliminar_juego.html', {'juego': juego})


class CustomLoginView(LoginView):
    template_name = 'juegos/login.html'

    def get_success_url(self):
        # Si es superusuario, redirigir al panel de administración
        if self.request.user.is_superuser:
            return reverse('index')  # Puedes redirigir a cualquier otra página especial para superusuarios
        # Si es un usuario normal, redirigir a la lista de productos
        return reverse('index')
    

from django.contrib.auth.models import User

@login_required
def perfil_usuario(request):
    if request.user.is_superuser:
        usuarios = User.objects.all()
    else:
        usuarios = None

    context = {
        'user': request.user,
        'usuarios': usuarios,
    }
    return render(request, 'juegos/perfil.html', context)

from django.contrib.auth.decorators import user_passes_test
from .forms import CategoriaForm

# Verifica si el usuario es administrador
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')  # Redirige a la página donde se listan las categorías
    else:
        form = CategoriaForm()
    return render(request, 'juegos/crear_categoria.html', {'form': form})
from .models import Categoria

@user_passes_test(is_admin)
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'juegos/listar_categorias.html', {'categorias': categorias})

@user_passes_test(is_admin)
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')  # Redirigir a la lista de categorías después de editar
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'juegos/editar_categoria.html', {'form': form, 'categoria': categoria})

@user_passes_test(is_admin)
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')  # Redirige a la lista de categorías después de eliminar
    return render(request, 'juegos/eliminar_categoria.html', {'categoria': categoria})


from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserCreationForm


@login_required
@user_passes_test(is_admin)
def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')
    else:
        form = UserCreationForm()
    return render(request, 'juegos/crear_usuario.html', {'form': form})

from django.contrib.auth.forms import UserChangeForm

@login_required
@user_passes_test(is_admin)
def editar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')
    else:
        form = UserChangeForm(instance=usuario)
    return render(request, 'juegos/editar_usuario.html', {'form': form, 'usuario': usuario})

@login_required
@user_passes_test(is_admin)
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('perfil_usuario')
    return render(request, 'juegos/eliminar_usuario.html', {'usuario': usuario})

from .forms import UserEditForm
@login_required
def editar_perfil(request):
    usuario = request.user  # Usa el usuario autenticado en lugar de buscar por pk
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')
    else:
        form = UserEditForm(instance=usuario)
    return render(request, 'juegos/editar_perfil.html', {'form': form})


from django.shortcuts import render
@login_required
def ver_carrito(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = sum(item.juego.precio * item.cantidad for item in items)
    
    context = {
        'items': items,
        'total': total,
    }

    return render(request, 'juegos/ver_carrito.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Juego, Carrito, ItemCarrito
from django.contrib import messages

@login_required
def agregar_al_carrito(request, juego_id):
    # Obtén el juego por ID
    juego = get_object_or_404(Juego, id=juego_id)

    # Obtén o crea el carrito para el usuario actual
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    # Imprimir el estado del carrito
    print(f"Carrito creado: {carrito} - Creado: {created}")

    try:
        # Obtén o crea el item en el carrito
        item_carrito, created = ItemCarrito.objects.get_or_create(
            carrito=carrito,
            juego=juego,
            defaults={'cantidad': 1}  # Se inicializa la cantidad a 1
        )

        # Verificar si se creó un nuevo item o se encontró uno existente
        if created:
            print(f"Creado nuevo item en el carrito: {item_carrito}")
        else:
            item_carrito.cantidad += 1  # Incrementa la cantidad
            item_carrito.save()  # Guarda el item actualizado
            print(f"Item existente en el carrito, cantidad actual: {item_carrito.cantidad}")

        # Verificar si el item se ha guardado en la base de datos
        if ItemCarrito.objects.filter(carrito=carrito, juego=juego).exists():
            print(f"El item {juego.nombre} se encuentra en el carrito.")
        else:
            print(f"El item {juego.nombre} NO se ha guardado en el carrito.")

    except Exception as e:
        print(f"Ocurrió un error al agregar el item al carrito: {e}")

    return redirect('ver_carrito')  # Redirige a la vista del carrito

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if item.carrito.usuario == request.user:
        item.delete()
    return redirect('ver_carrito')


    
def terror_view(request):
    juegos = Juego.objects.filter(categoria__nombre="Terror")
    return render(request, 'juegos/terror.html', {'juegos': juegos})

def aventuras_view(request):
    juegos = Juego.objects.filter(categoria__nombre='Aventuras')
    return render(request, 'juegos/aventuras.html', {'juegos': juegos})

def shooter_view(request):
    juegos = Juego.objects.filter(categoria__nombre='Shooter')
    return render(request, 'juegos/shooter.html', {'juegos': juegos})

def deportes_view(request):
    juegos = Juego.objects.filter(categoria__nombre='Deportes')
    return render(request, 'juegos/deportes.html', {'juegos': juegos})

def rpg_view(request):
    juegos = Juego.objects.filter(categoria__nombre='RPG')
    return render(request, 'juegos/rpg.html', {'juegos': juegos})

@login_required
def realizar_pedido(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    
    # Verificar si el carrito tiene elementos
    if carrito.itemcarrito_set.exists():
        # Crear un nuevo pedido para el carrito
        pedido = Pedido.objects.create(carrito=carrito)
        # Eliminar los elementos del carrito después de crear el pedido
        carrito.itemcarrito_set.all().delete()
        messages.success(request, 'Pedido realizado con éxito.')
        return redirect('confirmacion_pedido', pedido_id=pedido.id)
    else:
        messages.info(request, 'Tu carrito está vacío.')
        return redirect('ver_carrito')

def confirmacion_pedido(request, pedido_id):
    return render(request, 'juegos/confirmacion_pedido.html')