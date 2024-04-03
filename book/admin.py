from django.contrib import admin
from book.models import Book, Chapter, Tag

# Register your models here.
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Tag)