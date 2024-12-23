from django import forms
from .models import Books,Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name']


class BookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = '__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the book name'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter the book author'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the book price'})
        }