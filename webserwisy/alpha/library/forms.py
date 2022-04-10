from django import forms
from django.core.exceptions import ValidationError

from .models import Book

class AddBookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author_name = forms.CharField(max_length=200)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 5}),
        required=False
    )

    def clean_author_name(self):
        author_name = self.cleaned_data["author_name"]
        if author_name != "Adam Mickiewicz":
            raise ValidationError("Obsługujemy tylko książki Adama Mickiewicza")
        return author_name

class BookForm_ModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']
