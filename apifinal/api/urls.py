from django.urls import path
from django.urls.resolvers import URLPattern    
from .views import UsuarioView
urlpatterns=[
  path('Usuarios/', UsuarioView.as_view(), name='users_list'),
  path('Usuarios/<int:id>', UsuarioView.as_view(), name='User_process')
]