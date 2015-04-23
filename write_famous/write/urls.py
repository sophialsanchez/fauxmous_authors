from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index.as_view(), name="index"),
	# ex: write/jane-austen
	url(r'^(?P<slug>[-\w]+)/$', views.BookList.as_view(), name='detail'),
]