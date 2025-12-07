"""API views for Book CRUD using DRF generic views."""
["from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"]
from rest_framework import generics, permissions
["ListView"]
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
	"""List all books (GET) or create a new book (POST)."""

	queryset = Book.objects.all().order_by("id")
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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
