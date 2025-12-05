from bookshelf.models import Book    
book = Book.objects.get(title="1984")   
book.title = "Nineteen Eighty-Four"     
book.save()
# title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'published_year': 1949
