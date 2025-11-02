from bookshelf.models import Book
print(list(Book.objects.values())) 
# [{'id': 1, 'title': 'New Title', 'author': 'Jane Doe', 'published_year': 2025}, {'id': 2, 'title': '1984', 'author': 'George Orwell', 'published_year': 1949}] 
