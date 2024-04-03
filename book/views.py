from django.shortcuts import get_object_or_404
from django.views import generic
from book.forms import BookForm, ChapterForm
from book.models import Book, Chapter


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book'

    def get_queryset(self):
        return self.model.objects.all()


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
        return self.model.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
