from django.views.generic import TemplateView


class Inicio(TemplateView):
    template_name = "paginas/index.html"
    from django.views.generic import Campus
    
    class CampusCreate(CreateView):

        template_name = 'paginas/form.html'
        model = Campus
        fields = ['nome']
        sucess_url = reverse_lazy('index')

    class CursoCreate(CreateView):
        template_name = 'paginas/form.html'
        model = Curso
        fields = ['nome']
        sucess_url = reverse-lazy('index')

""