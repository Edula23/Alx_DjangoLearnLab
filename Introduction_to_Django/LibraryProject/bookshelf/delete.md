from bookshelf.models import Book
info = Book.objects.filter(id=2).delete() 