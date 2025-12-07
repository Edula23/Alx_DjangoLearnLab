from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author, Book
# ["response.data"]

class BookAPITests(APITestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(username="tester", password="pass1234")
		self.author = Author.objects.create(name="Jane Doe")
		self.book1 = Book.objects.create(title="Alpha", publication_year=2020, author=self.author)
		self.book2 = Book.objects.create(title="Beta", publication_year=2010, author=self.author)

	def test_list_books(self):
		url = reverse("book-list")
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.assertEqual(len(resp.data), 2)

	def test_create_requires_auth(self):
		url = reverse("book-list")
		payload = {"title": "Gamma", "publication_year": 2021, "author": self.author.id}
		resp = self.client.post(url, payload, format="json")
		self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_create_book_authenticated(self):
		self.client.login(username="tester", password="pass1234")
		url = reverse("book-list")
		payload = {"title": "Gamma", "publication_year": 2021, "author": self.author.id}
		resp = self.client.post(url, payload, format="json")
		self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Book.objects.count(), 3)

	def test_filter_by_title(self):
		url = reverse("book-list") + "?title=Alpha"
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.assertEqual(len(resp.data), 1)
		self.assertEqual(resp.data[0]["title"], "Alpha")

	def test_search_by_title(self):
		url = reverse("book-list") + "?search=bet"
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.assertEqual(len(resp.data), 1)
		self.assertEqual(resp.data[0]["title"], "Beta")

	def test_ordering_desc(self):
		url = reverse("book-list") + "?ordering=-publication_year"
		resp = self.client.get(url)
		years = [item["publication_year"] for item in resp.data]
		self.assertEqual(years, sorted(years, reverse=True))

	def test_update_requires_auth(self):
		url = reverse("book-update", args=[self.book1.id])
		resp = self.client.put(url, {"title": "Alpha2", "publication_year": 2020, "author": self.author.id}, format="json")
		self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_update_authenticated(self):
		self.client.login(username="tester", password="pass1234")
		url = reverse("book-update", args=[self.book1.id])
		resp = self.client.put(url, {"title": "Alpha2", "publication_year": 2020, "author": self.author.id}, format="json")
		self.assertEqual(resp.status_code, status.HTTP_200_OK)
		self.book1.refresh_from_db()
		self.assertEqual(self.book1.title, "Alpha2")

	def test_delete_requires_auth(self):
		url = reverse("book-delete", args=[self.book2.id])
		resp = self.client.delete(url)
		self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_delete_authenticated(self):
		self.client.login(username="tester", password="pass1234")
		url = reverse("book-delete", args=[self.book2.id])
		resp = self.client.delete(url)
		self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

# Create your tests here.
