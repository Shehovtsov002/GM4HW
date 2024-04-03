from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:id>/', views.BookDetailView.as_view()),
    path('books/<int:id>/update/', views.BookUpdateView.as_view()),
    path('books/<int:id>/delete/', views.BookDeleteView.as_view()),
    path('create_book/', views.BookCreateView.as_view()),
    path('search/', views.SearchView.as_view(), name='search'),
]
