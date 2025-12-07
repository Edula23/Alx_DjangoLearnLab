"""API views for Book CRUD with filtering, search, and ordering."""

from rest_framework import generics, permissions, filters

from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
	"""List all books (GET) or create a new book (POST)."""

	queryset = Book.objects.all().order_by("id")
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	# Enable filtering, search, and ordering
	filter_backends = [
		filters.SearchFilter,
		filters.OrderingFilter,
	]
	filterset_fields = ["title", "author", "publication_year"]
	search_fields = ["title", "author__name"]
	ordering_fields = ["title", "publication_year", "id"]
	ordering = ["id"]


class BookDetailView(generics.RetrieveAPIView):
	"""Retrieve a single book by ID (read-only)."""

	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.AllowAny]


class BookUpdateView(generics.UpdateAPIView):
	"""Update an existing book; requires authentication."""

	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
	"""Delete a book; requires authentication."""

	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticated]
