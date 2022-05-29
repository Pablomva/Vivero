from django.shortcuts import render,redirect
from Vivero.forms import FormUsuarios, RegistroFormulario
from Vivero.models import Arboles,Arbustos,Herbaceas,Semillas,Usuarios
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def inicio(request):
    return render(request, 'Vivero/inicio.html')

def arboles(request):
    return render(request, 'Vivero/arboles.html')

def arbustos(request):
    return render(request, 'Vivero/arbustos.html')

def herbaceas(request):
    return render(request, 'Vivero/herbaceas.html')

def semillas(request):
    return render(request, 'Vivero/semillas.html')

def usuarios(request):
    if request.method == "POST":
        mi_form = FormUsuarios(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            usu= Usuarios(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
                pais=info["pais"],
                provincia=info["provincia"],
                ciudad=info["ciudad"],
            )
            usu.save()
            return redirect("Inicio")

    mi_form = FormUsuarios()
    
    return render(request, "Vivero/usuarios.html",{"form": mi_form})

class ArbolesList(ListView):

    model= Arboles
    template_name= "Vivero/listaarboles.html"

class ArbolesDetalle(DetailView):

    model= Arboles
    template_name="Vivero/arboles_detalles.html"

class ArbolesCreacion(CreateView):

    model=Arboles
    success_url= "/Vivero/arboles/list"
    fields= ['familia','nombre_cientifico','nombre_comun','tipo_canopia','forma','altura_media_en_metros'] 
    
class ArbolesUpdate(UpdateView):

    model= Arboles
    success_url= "/Vivero/arboles/list"
    fields= ['familia','nombre_cientifico','nombre_comun','tipo_canopia','forma','altura_media_en_metros']

class ArbolesDelete(DeleteView):

    model= Arboles
    success_url= "/Vivero/arboles/list"

def register(request):

    if request.method =='POST':

        form= RegistroFormulario(request.POST)

        if form.is_valid():

            username =form.cleaned_data ['username']
            form.save()

            return render (request,'Vivero/inicio.html', {'mensaje': "Usuario creado"})

    else:

        form= RegistroFormulario()

    return render(request, 'Vivero/registro.html' , {'form':form})


def login_request(request):

    if request.method == 'POST': 

        form = AuthenticationForm(request, data = request.POST) 

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')   
            contra=form.cleaned_data.get('password')    

            user=authenticate(username=usuario, password=contra)   

            if user:    
                login(request, user)   

               
                return render(request, "Vivero/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:  

           
    
            return render(request, "Vivero/inicio.html", {'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() 

    return render(request, "Vivero/login.html", {'form':form})

def about(request):
    return render(request,'Vivero/aboutme.html')

  






    


