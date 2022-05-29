from django.urls import path
from Vivero import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio, name='Inicio'),
    path('arboles/', views.arboles, name='Arboles'),
    path('arbustos/', views.arbustos, name='Arbustos'),
    path('herbaceas/', views.herbaceas, name='Herbaceas'), 
    path('semillas/',views.semillas, name='Semillas'),
    path ('usuarios/', views.usuarios, name='Usuarios'),
    path('arboles/list',views.ArbolesList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ArbolesDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ArbolesCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ArbolesUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ArbolesDelete.as_view(), name='Delete'),
    path('login/', views.login_request, name= 'Login'),
    path('logout', LogoutView.as_view (template_name='Vivero/logout.html'), name='Logout'),
    path('registro', views.register, name = 'Registro'), 
    path('aboutme',views.about, name='Sobre mí'),
]


    