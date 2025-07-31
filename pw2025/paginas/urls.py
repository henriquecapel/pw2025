from django.urls import path
from .views import Inicio, ClienteCreate, ClienteUpdate, ClienteDelete, FotografoCreate, FotografoUpdate, FotografoDelete, EstudioCreate, EstudioUpdate, EstudioDelete, SessaoFotoCreate, SessaoFotoUpdate, SessaoFotoDelete


urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
    
   
    path("adicionar/cliente/", ClienteCreate.as_view(), name="inserir-cliente"),
    path("adicionar/fotografo/", FotografoCreate.as_view(), name="inserir-fotografo"),
    path("adicionar/estudio/", EstudioCreate.as_view(), name="inserir-estudio"),
    path("adicionar/sessao/", SessaoFotoCreate.as_view(), name="inserir-sessao"),

####################################################

    path("editar/cliente/<int:pk>/", ClienteUpdate.as_view(), name="editar-cliente"),
    path("editar/fotografo/<int:pk>/", FotografoUpdate.as_view(), name="editar-fotografo"),
    path("editar/estudio/<int:pk>/", EstudioUpdate.as_view(), name="editar-estudio"),
    path("editar/sessao/<int:pk>/", SessaoFotoUpdate.as_view(), name="editar-sessao"),
    
#####################################################

    # path("excluir/sobre-nós/", SobrenósDelete.as_view(), name="excluir-Sobre-nós"),
    path("excluir/cliente/<int:pk>/", ClienteDelete.as_view(), name="excluir-cliente"),
    path("excluir/fotografo/<int:pk>/", FotografoDelete.as_view(), name="excluir-fotografo"),
    path("excluir/estudio/<int:pk>/", EstudioDelete.as_view(), name="excluir-estudio"),
    path("excluir/sessao/<int:pk>/", SessaoFotoDelete.as_view(), name="excluir-sessao"),


]
