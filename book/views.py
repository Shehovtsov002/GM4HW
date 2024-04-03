from django.shortcuts import get_object_or_404
from django.views import generic
from book.forms import BookForm, ChapterForm
from book.models import Book, Chapter, Tag


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book'

    def get_queryset(self):
        tag_name = self.request.GET.get('tag')
        if tag_name:
            return self.model.objects.filter(tags__name__in=[tag_name]).order_by('-id')
        else:
            return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=book_id)


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'book_crud/book_add.html'
    form_class = BookForm
    success_url = '/books/'

    def form_valid(self, form):
        return super(BookCreateView, self).form_valid(form)


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'book_crud/book_update.html'
    form_class = BookForm
    success_url = '/books/'

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form)

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=book_id)


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'book_crud/book_delete.html'
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=book_id)


class SearchView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book'
    paginate_by = '5'

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
