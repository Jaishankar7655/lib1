from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from app.forms import BooksForm
from app.models import Books

# Create your views here.
def addbook(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['Book_Title']
            author = form.cleaned_data['Author_name']
            isbn = form.cleaned_data['ISBN_Number']
            print(name, author, isbn)
            form.save()
            return render(request, 'app/success.html')
    else:
        form = BooksForm()
    return render(request, 'app/addbook.html', {'form': form})

def success(request):
    return render(request, 'app/success.html')

def main(request):
    return render(request, 'app/main.html')

def allbooks(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        # Search in multiple fields using Q objects
        books = Books.objects.filter(
            Q(Book_Title__icontains=search_query) |
            Q(Author_name__icontains=search_query) |
            Q(ISBN_Number__icontains=search_query) |
            Q(Genre__icontains=search_query) |
            Q(Publisher__icontains=search_query)
        ).distinct()
    else:
        books = Books.objects.all()
    
    context = {
        'books': books,
        'search_query': search_query
    }
    return render(request, 'app/allbooks.html', context)

def viewbook(request, pk):
    book = get_object_or_404(Books, id=pk)
    return render(request, 'app/viewbook.html', {'book': book})