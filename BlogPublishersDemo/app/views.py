"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }))

def books(request):
    """Renders the books page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/books.html',
        context_instance = RequestContext(request,
        {
            'title':'Books',
            'message':'Your books page.',
            'year':datetime.now().year,
        }))

def books_detail(request, id):
    """Renders the books page."""
    assert isinstance(request, HttpRequest)

    current_book = Book.objects.filter(id=id).first()


    return render(request,
        'app/books-detail.html',
        context_instance = RequestContext(request, {
            "book": current_book }))

def publishers(request):
    """Renders the publishers page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/publishers.html',
        context_instance = RequestContext(request,
        {
            'title':'Publishers',
            'message':'Your publishers page.',
            'year':datetime.now().year,
        }))
