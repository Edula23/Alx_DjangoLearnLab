from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic import DetailView
# Create your views here.
def listBooks(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)
class libraryDetailView(DetailView):
    model = Library
    template_name = 'books/library_detail.html'