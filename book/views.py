from django.shortcuts import render, get_object_or_404
from book.models import Book


def book_list(request):
    if request.method == 'GET':
        query = Book.objects.all()
        return render(request, 'book_list.html', {'query': query})


def book_detail(request, book_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'book_detail.html', {'book': book})
