from django import forms
from app.models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'Book_Title',
            'Author_name',
            'ISBN_Number',
            'Book_Description',
            'Genre',
            'Publisher',
            'Publication_Year',
            'copies_available',
            'rack_number',
            'Book_Url',
            'thumbnail',
            'Book_PDF',
        ]
        
        labels = {
            'Book_Title': 'Book Title',
            'Author_name': 'Author Name',
            'ISBN_Number': 'ISBN Number',
            'Book_Description': 'Description',
            'Genre': 'Genre',
            'Publisher': 'Publisher',
            'Publication_Year': 'Year of Publication',
            'copies_available': 'Available Copies',
            'rack_number': 'Rack Number',
            'Book_Url': 'Book URL',
            'thumbnail': 'Book Cover Image',
            'Book_PDF': 'PDF File',
        }
        
        widgets = {
            'Book_Title': forms.TextInput(attrs={
                'class': 'form-control',
                
            }),
            'Author_name': forms.TextInput(attrs={
                'class': 'form-control',
               
            }),
            'ISBN_Number': forms.TextInput(attrs={
                'class': 'form-control',
                
            }),
            'Book_Description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter book description'
            }),
            
            'Publisher': forms.TextInput(attrs={
                'class': 'form-control',
               
            }),
            'Publication_Year': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'copies_available': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'Enter number of copies available'
            }),
            'rack_number': forms.TextInput(attrs={
                'class': 'form-control',
                
            }),
            'Book_Url': forms.URLInput(attrs={
                'class': 'form-control',
              
            }),
            'thumbnail': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'Book_PDF': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '*'
            }),
        }