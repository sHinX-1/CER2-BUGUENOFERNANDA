from django.urls import path
from sesion import views        # Aqui se importan las vistas desde la app creada
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio', views.inicio),
    path('nosotros', views.nosotros, name='sobre-nosotros'),
    path('mascotas', views.mascotas, name='mascotas'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='sesion/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]