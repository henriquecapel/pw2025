from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Fotografo, Estudio, SessaoFoto
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView


class Inicio(TemplateView):
    template_name = "paginas/index.html"


class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'telefone', 'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class FotografoCreate(CreateView):
    model = Fotografo
    fields = ['nome', 'especialidade', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class EstudioCreate(CreateView):
    model = Estudio
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class SessaoFotoCreate(CreateView):
    model = SessaoFoto
    fields = ['data', 'horario', 'tipo', 'duracao', 'cliente', 'fotografo', 'estudio', 'finalizado', 'valor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}


#############################################################


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome', 'telefone', 'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}


class FotografoUpdate(UpdateView):
    model = Fotografo
    fields = ['nome', 'especialidade', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class EstudioUpdate(UpdateView):
    model = Estudio
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class SessaoFotoUpdate(UpdateView):
    model = SessaoFoto
    fields = ['data', 'horario', 'tipo', 'duracao', 'cliente', 'fotografo', 'estudio', 'finalizado', 'valor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

#########################################################

class ClienteDelete(DeleteView):
    model = Cliente
    fields = ['nome', 'telefone', 'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}


class FotografoDelete(DeleteView):
    model = Fotografo
    fields = ['nome', 'especialidade', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class EstudioDelete(DeleteView):
    model = Estudio
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class SessaoFotoDelete(DeleteView):
    model = SessaoFoto
    fields = ['data', 'horario', 'tipo', 'duracao', 'cliente', 'fotografo', 'estudio', 'finalizado', 'valor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

############################################################

class PerfilCliente(LoginRequiredMixin, ListView):
    Model = Cliente
    fields = ['nome', 'LoginRequiredMixin, ListViewail']
    template_name = 'paginas/form.html'
   
class PerfilFotografo(LoginRequiredMixin, ListView):
    model = Fotografo
    fields = ['nome', 'especialidade', 'telefone']
    template_name = 'paginas/form.html'
  
class PerfilEstudioD(LoginRequiredMixin, ListView):
    model = Estudio
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'paginas/form.html'
   

class PerfilSessaoFoto(LoginRequiredMixin, ListView):
    model = SessaoFoto
    fields = ['data', 'horario', 'tipo', 'duracao', 'cliente', 'fotografo', 'estudio', 'finalizado', 'valor']
    template_name = 'paginas/form.html'
 
  ##############################################################

class CriarClienteView(SuccessMessageMixin, CreateView):
    model = Cliente
    fields = ['nome', 'matricula', 'cpf', 'email', 'telefone']
    success_url = '/alunos/'
    success_message = "cliente criado com sucesso!"

class PerfilFotografo(SuccessMessageMixin, CreateView):
    model = Fotografo
    fields = ['nome', 'especialidade', 'telefone']
    success_url = '/alunos/'
    success_message = "Perfil fotografo criado com sucesso!"
class PerfilEstudioD(SuccessMessageMixin, CreateView):
    model = Estudio
    fields = ['nome', 'endereco', 'telefone']
    success_url = '/alunos/'
    success_message = "Estudio criado com sucesso!"

class PerfilSessaoFoto(SuccessMessageMixin, CreateView):
    model = SessaoFoto
    fields = ['data', 'horario', 'tipo', 'duracao', 'cliente', 'fotografo', 'estudio', 'finalizado', 'valor']
    success_url = '/alunos/'
    success_message = "Sessão criado com sucesso!"