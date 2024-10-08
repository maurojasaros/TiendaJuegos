# Generated by Django 5.1 on 2024-09-27 18:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'categorias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipo_usuarios',
            },
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'carritos',
            },
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='juegos', to='juegos.categoria')),
            ],
            options={
                'db_table': 'juegos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.carrito')),
                ('juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.juego')),
            ],
            options={
                'db_table': 'items_carrito',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.carrito')),
            ],
            options={
                'db_table': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='juegos.tipousuario')),
            ],
            options={
                'db_table': 'perfiles_usuarios',
            },
        ),
    ]
