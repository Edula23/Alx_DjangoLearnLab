from models import Book
from models import Library
from models import Librarian

books_by_author = Book.objects.filter(author='John Doe')
booksInLibrary = Library.objects.all()
librarianInLibrary = Librarian.objects.filter(library = 'lib')

