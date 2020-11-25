from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from usuarios.forms import CustomUserCreationForm


class CadastrarUsuarioView(LoginRequiredMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'usuarios/form_usuario.html'
    success_url = '/usuarios/'

class ListarUsuariosView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usuarios/listar_usuarios.html'
    paginate_by = 10

class EditarUsuarioView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'usuarios/form_usuario.html'
    success_url = '/usuarios/'

class RemoverUsuarioView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = '/usuarios/'


class LoginUsuarioView(LoginView):
    template_name = 'usuarios/form_login.html'
    success_url = '/vendas/'
    redirect_authenticated_user = '/vendas/'

def logout_user(request):
    logout(request)
    return redirect('logar_usuario')