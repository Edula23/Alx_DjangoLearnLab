books = Book.objects.all() 
books_by_library = Book.objects.filter(library='John Doe')
librarian_by_library = Librarian.objects.filter(library='John Doe')