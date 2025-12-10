from models import Book
from models import Library
from models import Librarian

books_by_author = Book.objects.filter(author='John Doe')
library = Library.objects.get(name="library_name")
bookInLIbrary = library.books.all()
librarianInLibrary = library.librarian


