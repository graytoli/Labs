from django.shortcuts import render
from django.db.models import Q

from .models import Author, Book

def find_matches(request):
    search_term = request.GET.get('query', '')
    books = Book.objects.filter(Q(title__icontains=search_term) | Q(author__name__icontains=search_term))
    print(books)
    return render(request, 'find_matches.html', {'books': books})

