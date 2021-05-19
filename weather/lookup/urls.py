"""
cualquier pagina creada aqui es conectada al lookup folder
asi cuando se quiera remover el lookup folder, todos estos urls se remueven solos
"""

#se hace referencia a las views que estan dentro
# del folder lookup

from django.urls import path
from . import views #se importa el file views

urlpatterns = [
    path('', views.home ,name="home"),
    path('about/', views.about ,name="about"),
]
