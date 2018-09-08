"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from BestFriends.settings import prime_number
from BestFriends.settings import compute_gap
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'biggest_prime_number':prime_number[0],
            'time_to_next_prime':compute_gap

        })

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Please do not hesitate to contact us with the information below.',
            'year':datetime.now().year,
        })

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        {
            'title':'About',
            'message':'This project is being developed by Kexin Huang & Dewei Liu who are the best friends in the world, since 14 Aug 2018!',
            'content':'',
            'year':datetime.now().year,
        })
