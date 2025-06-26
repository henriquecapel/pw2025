from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views 

urlpatterns = [
    
    # criar rota para página de login
    
    path("login/", auth_views.LoginView.as_view(
        template_name = 'paginas/form.html',
        extra_context = {
            'Cadastro Fotografia': 'Atualização de fotos', 
            'Enviar dados': 'protocolar',
            }

    ), name="login"),

       path("senha/", auth_views.PasswordChangeView.as_view(
        template_name = 'paginas/form.html',
        extra_context = {
            'Cadastro Fotografia': 'atualizar senha', 
            'Enviar dados': 'salvar',
            }

    ), name="senha"),
    
    
    #criar rota de logout
    path("logout", auth_views.LogoutView.as_view(), name = "logout"),
    
    path("", Inicio.as_view(), name="inicio"),
    path('sobre/', SobreView.as_view(), name='sobre'), 
    path("adicionar/cliente/", ClienteCreate.as_view(), name="inserir-cliente"),
    path("adicionar/fotografo/", FotografoCreate.as_view(), name="inserir-fotografo"),
    path("adicionar/estudio/", EstudioCreate.as_view(), name="inserir-estudio"),
    path("adicionar/sessao/", SessaoFotoCreate.as_view(), name="inserir-sessao"),

    path("editar/cliente/<int:pk>/", ClienteUpdate.as_view(), name="editar-cliente"),
    path("editar/fotografo/<int:pk>/", FotografoUpdate.as_view(), name="editar-fotografo"),
    path("editar/estudio/<int:pk>/", EstudioUpdate.as_view(), name="editar-estudio"),
    path("editar/sessao/<int:pk>/", SessaoFotoUpdate.as_view(), name="editar-sessao"),

    path("excluir/cliente/<int:pk>/", ClienteDelete.as_view(), name="excluir-cliente"),
    path("excluir/fotografo/<int:pk>/", FotografoDelete.as_view(), name="excluir-fotografo"),
    path("excluir/estudio/<int:pk>/", EstudioDelete.as_view(), name="excluir-estudio"),
    path("excluir/sessao/<int:pk>/", SessaoFotoDelete.as_view(), name="excluir-sessao"),

    path("listar/cliente/", ClienteListView.as_view(), name="listar-clientes"),





]
