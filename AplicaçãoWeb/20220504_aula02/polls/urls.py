from django.urls import path

# Importamos o modo viwes que esta no memso deiretóirio de 'urls.py'
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
