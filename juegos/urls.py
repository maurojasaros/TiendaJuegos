from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, agregar_al_carrito, ver_carrito, eliminar_del_carrito, realizar_pedido

urlpatterns = [
    # Página principal del sitio
    path('', views.index, name='index'),
    
    # Página de formulario (probablemente para registro o login)
    path('formulario/', views.formulario, name='formulario'),
    
    # Vistas para diferentes categorías de juegos
    path('categoria/terror/', views.terror_view, name='categoria_terror'),
    path('categoria/aventuras/', views.aventuras_view, name='categoria_aventuras'),
    path('categoria/shooter/', views.shooter_view, name='categoria_shooter'),
    path('categoria/deportes/', views.deportes_view, name='categoria_deportes'),
    path('categoria/rpg/', views.rpg_view, name='categoria_rpg'),
    
    # CRUD juegos
    path('lista_juegos/', views.listar_juegos, name='listar_juegos'),
    path('juegos/crear/', views.crear_juego, name='crear_juego'),
    path('juegos/ver/<int:pk>/', views.ver_juego, name='ver_juego'),
    path('juegos/editar/<int:pk>/', views.editar_juego, name='editar_juego'),
    path('juegos/eliminar/<int:pk>/', views.eliminar_juego, name='eliminar_juego'),
    
    # Autenticación de usuarios: login y logout
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # CRUD administración de categorías
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('lista_categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),
    
    # CRUD Administración de usuarios: listar(perfil con admin), creación, edición y eliminación
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    
    # Recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='juegos/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='juegos/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='juegos/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='juegos/password_reset_complete.html'), name='password_reset_complete'),
    
    # Edición del perfil del usuario
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    
    # CRUD Carrito de compras: agregar ítems, ver el carrito, eliminar ítems y realizar un pedido
    path('agregar_al_carrito/<int:juego_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('realizar_pedido/', realizar_pedido, name='realizar_pedido'),
    
    # Confirmación del pedido realizado
    path('confirmacion_pedido/<int:pedido_id>/', views.confirmacion_pedido, name='confirmacion_pedido'),

    # API
    path('api/juegos/', views.juego_list, name='juegos_api'),  # Para obtener y crear juegos
    path('api/juegos/<int:juego_id>/', views.juego_detail, name='juego_detail'),  # GET, PUT y DELETE para un juego específico
    path('api/categorias/', views.categoria_list, name='categoria-list'),
    path('api/categorias/<int:pk>/', views.categoria_detail, name='categoria-detail'),
    
    # Consolas de videojuegos
    path('consolas/', views.consolas_videojuegos, name='consolas_videojuegos'),
    path('juego/detalle/<int:game_id>/', views.detalles_juego, name='detalles_juego'),
]
    
