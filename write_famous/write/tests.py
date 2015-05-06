from django.test import TestCase
from write.models import Book

# Create your tests here.
class BookTests(TestCase):
	def test_book_author(self):
		"""The book author should match a string of that author's name."""
		test_book = Book.objects.create(book_author="Joanne Smith", book_title="A Tale of Two Tests", 
		book_text="It was the best of tests, it was the worst of tests", slug="a-tale-of-two-tests")
		self.assertEqual(Book.objects.get(book_author="Joanne Smith").book_author, "Joanne Smith")
	
	def test_book_title(self):
		"""The book title should match a string of that title."""
		test_book = Book.objects.create(book_author="Joanne Smith", book_title="A Tale of Two Tests", 
		book_text="It was the best of tests, it was the worst of tests", slug="a-tale-of-two-tests")
		self.assertEqual(Book.objects.get(book_author="Joanne Smith").book_title, "A Tale of Two Tests")

	def test_book_text(self):
		"""The book text should match a string of that text."""
		test_book = Book.objects.create(book_author="Joanne Smith", book_title="A Tale of Two Tests", 
		book_text="It was the best of tests, it was the worst of tests", slug="a-tale-of-two-tests")
		self.assertEqual(Book.objects.get(book_author="Joanne Smith").book_text, "It was the best of tests, it was the worst of tests")
		
	def test_slug(self):
		"""The book slug should match a string of that slug."""
		test_book = Book.objects.create(book_author="Joanne Smith", book_title="A Tale of Two Tests", 
		book_text="It was the best of tests, it was the worst of tests", slug="a-tale-of-two-tests")
		self.assertEqual(Book.objects.get(book_author="Joanne Smith").slug, "a-tale-of-two-tests")
		