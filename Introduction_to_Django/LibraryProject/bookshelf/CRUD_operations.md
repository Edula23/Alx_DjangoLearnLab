create
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", published_year=1949)
# created new book instance
retrieve
from bookshelf.models import Book
print(list(Book.objects.values())) 
# [{'id': 1, 'title': 'New Title', 'author': 'Jane Doe', 'published_year': 2025}, {'id': 2, 'title': '1984', 'author': 'George Orwell', 'published_year': 1949}] 
update
from bookshelf.models import Book    
b = Book.objects.get(title="1984")   
b.title = "Nineteen Eighty-Four"     
b.save()
# title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'published_year': 1949
delete
info = Book.objects.filter(id=2).delete() 