from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from book.forms import BookForm
from book.models import Book


def book_list_view(request):
    if request.method == 'GET':
        query = Book.objects.all()
        return render(request, 'book_list.html', {'query': query})


def book_detail_view(request, book_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'book_detail.html', {'book': book})


def book_add_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Answer create successfully</h1>')
    else:
        form = BookForm()
    return render(request, template_name='book_crud/book_add.html', context={'form': form})


def book_update_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Book updated successfully</h1>')
    else:
        form = BookForm(instance=book)
    return render(request, template_name='book_crud/book_update.html', context={'form': form})


def book_delete_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return HttpResponse('<h1>Book deleted successfully</h1>')
