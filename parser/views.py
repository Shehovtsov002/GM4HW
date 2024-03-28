from django.views import generic
from django.http import HttpResponse
from . import models, forms


class ParsingView(generic.FormView):
    template_name = 'parsing/parsing_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse("<h1>Parsing successfully</h1>")
        else:
            return super(ParsingView, self).post(request, *args, **kwargs)


class HouseListView(generic.ListView):
    template_name = 'parsing/house_list.html'
    context_object_name = 'house'
    model = models.HouseParser

    def get_queryset(self):
        return self.model.objects.all()


class ItemListView(generic.ListView):
    template_name = 'parsing/item_list.html'
    context_object_name = 'bazar'
    model = models.BazarParser

    def get_queryset(self):
        return self.model.objects.all()
