"""
Definition of urls for BlogPublishersDemo.
"""

from django.conf.urls import patterns, url
from app.views import GreetingView

urlpatterns = patterns('',
    url(r'^$', 'app.views.home', name='home'),
    url(r'^books$', 'app.views.books', name='books'),
    url(r'^books/(?P<id>\d+)/$', 'app.views.books_detail', name='books'),
    url(r'^publishers', 'app.views.publishers', name='publishers'),
    url(r'^example/', GreetingView.as_view(greeting="Test test")))


