from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Fotografo, Estudio, SessaoFoto

class Inicio(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'
    

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'telefone', 'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('ListarClientes')
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
    success_url = reverse_lazy('ListarClientes')
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

########################################

class ClienteDelete(DeleteView):
    model = Cliente
    fields = ['nome', 'telefone', 'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('ListarClientes')
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
    

class ClienteListView(ListView):
    model = Cliente
    template_name = 'paginas/Listas/ListarClientes.html'
   