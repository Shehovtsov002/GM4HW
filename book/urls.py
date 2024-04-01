from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('books/', views.book_list_view, name='book_list'),
    path('books/<int:book_id>/', views.book_detail_view),
    path('books/<int:book_id>/update/', views.book_update_view),
    path('books/<int:book_id>/delete/', views.book_delete_view),
    path('create_book/', views.book_add_view),
]
