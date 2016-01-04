"""
Definition of urls for BlogPublishersDemo.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

urlpatterns = patterns('',
    url(r'^$', 'app.views.home', name='home'),
    url(r'^books$', 'app.views.books', name='books'),
    url(r'^books/(?P<id>\d+)/$', 'app.views.books_detail', name='books'),
    url(r'^publishers', 'app.views.publishers', name='publishers'),)
