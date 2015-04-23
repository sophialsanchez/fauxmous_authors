from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from write.models import Book


class index(ListView):
	model = Book # tells the view which model to act on
	template_name = 'write/index.html'
	context_object_name = 'book_list'
	def get_queryset(self):
		books = Book.objects.order_by('book_author')
		return books


class BookList(DetailView):
	model = Book
	template_name = 'write/detail.html'
	
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(BookList, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['book_list'] = Book.objects.all()
		return context