from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormUsuarios(forms.Form):
    nombre=forms.CharField(max_length=255)
    apellido=forms.CharField(max_length=255)
    email=forms.EmailField()
    pais=forms.CharField(max_length=255)
    provincia=forms.CharField(max_length=255)
    ciudad=forms.CharField(max_length=255)

class RegistroFormulario(UserCreationForm):

    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:

        model= User
        fields = ['username', 'email', 'password1','password2']

