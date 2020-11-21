from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView

from usuarios.forms import CustomUserCreationForm


class CadastrarUsuarioView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'usuarios/form_usuario.html'
    success_url = 'usuarios/'
