from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re
from .models import Juego, Categoria

class RegistroForm(forms.Form):
    # Formulario para el registro de nuevos usuarios
    nombre_usuario = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )
    apellido = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'})
    )
    edad = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'})
    )
    direccion = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'})
    )
    ciudad = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'})
    )

    def clean_nombre_usuario(self):
        # Verifica si el nombre de usuario ya está en uso
        nombre_usuario = self.cleaned_data.get('nombre_usuario')
        if User.objects.filter(username=nombre_usuario).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        return nombre_usuario

    def clean_email(self):
        # Verifica si el correo electrónico ya está registrado
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_password(self):
        # Valida la contraseña según ciertos criterios
        password = self.cleaned_data.get('password')
        if len(password) < 6 or len(password) > 18:
            raise ValidationError("La contraseña debe tener entre 6 y 18 caracteres.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r'\d', password):
            raise ValidationError("La contraseña debe contener al menos un dígito.")
        return password

    def clean_confirm_password(self):
        # Verifica que la confirmación de la contraseña coincida con la contraseña
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden.")
        return confirm_password

    def clean_edad(self):
        # Verifica que la edad sea mayor de 18 años
        edad = self.cleaned_data.get('edad')
        if edad and edad < 18:
            raise ValidationError("Debes ser mayor de 18 años para registrarte.")
        return edad
    
class JuegoForm(forms.ModelForm):
    # Formulario para crear y editar objetos Juego
    class Meta:
        model = Juego
        fields = ['nombre', 'descripcion', 'precio', 'categoria']

class CategoriaForm(forms.ModelForm):
    # Formulario para crear y editar objetos Categoria
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class UserCreationForm(forms.ModelForm):
    # Formulario para la creación de un nuevo usuario
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        # Verifica que la contraseña y su confirmación coincidan
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

