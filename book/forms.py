from django import forms

from book.models import Book, Chapter


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'
