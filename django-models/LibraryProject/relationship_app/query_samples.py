from models import Book
from models import Library
from models import Librarian
from models import Author
author_name = "Eden"
library_name = "Digital"

author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
library = Library.objects.get(name=library_name)
bookInLIbrary = library.books.all()
librarianInLibrary = Librarian.objects.get(library= library)
librarian = Library.objects.get(librarian = librarianInLibrary)


