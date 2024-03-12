from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from book.models import Book


def book_list(request):
    if request.method == 'GET':
        query = Book.objects.all()
        return render(request, 'book_list.html', {'query': query})
