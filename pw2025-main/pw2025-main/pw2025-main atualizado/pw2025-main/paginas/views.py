from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Fotografo, Estudio, SessaoFoto

from django.contrib.auth.mixins import LoginRequiredMixin


class Inicio(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'
    

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nome', 'telefone', 'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('ListarClientes')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}


class FotografoCreate(LoginRequiredMixin, CreateView):
    model = Fotografo
    fields = ['nome', 'especialidade', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class EstudioCreate(LoginRequiredMixin, CreateView):
    model = Estudio
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class SessaoFotoCreate(LoginRequiredMixin, CreateView):
    model = SessaoFoto
    fields = ['data', 'horario', 'tipo', 'duracao', 'cliente', 'fotografo', 'estudio', 'finalizado', 'valor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}


#############################################################


class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nome', 'telefone', 'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('ListarClientes')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}


class FotografoUpdate(LoginRequiredMixin, UpdateView):
    model = Fotografo
    fields = ['nome', 'especialidade', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class EstudioUpdate(LoginRequiredMixin, UpdateView):
    model = Estudio
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class SessaoFotoUpdate(LoginRequiredMixin, UpdateView):
    model = SessaoFoto
    fields = ['data', 'horario', 'tipo', 'duracao', 'cliente', 'fotografo', 'estudio', 'finalizado', 'valor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

########################################

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    fields = ['nome', 'telefone', 'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('ListarClientes')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}


class FotografoDelete(LoginRequiredMixin, DeleteView):
    model = Fotografo
    fields = ['nome', 'especialidade', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class EstudioDelete(LoginRequiredMixin, DeleteView):
    model = Estudio
    fields = ['nome', 'endereco', 'telefone']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}

class SessaoFotoDelete(LoginRequiredMixin, DeleteView):
    model = SessaoFoto
    fields = ['data', 'horario', 'tipo', 'duracao', 'cliente', 'fotografo', 'estudio', 'finalizado', 'valor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('inicio')
    extra_content = {'Cadastro Fotografia': 'Atualização de fotos', 'Enviar dados': 'protocolar',}
    

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'paginas/Listas/ListarClientes.html'
   