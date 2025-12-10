from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
# Create your views here.
def listBooks(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)
class libraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'