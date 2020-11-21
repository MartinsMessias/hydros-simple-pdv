from django.urls import path

from usuarios.views import *

urlpatterns = [
    path('', ListarUsuariosView.as_view(), name='listar_usuarios'),
    path('cadastrar/', CadastrarUsuarioView.as_view(), name='cadastrar_usuario'),
    path('editar/<str:pk>', EditarUsuarioView.as_view(), name='editar_usuario'),
    path('remover/<str:pk>', RemoverUsuarioView.as_view(), name='remover_usuario'),
    path('login/', LoginUsuarioView.as_view(), name='logar_usuario'),
    path('logout/', logout_user, name='logar_usuario'),
]
