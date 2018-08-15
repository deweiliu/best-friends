"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    finish_time = datetime.strptime("31 08 2018 23:59:59","%d %m %Y %H:%M:%S")
    duration = finish_time - datetime.now()
    duration_str = "%d days, %d hours, %d minutes and %d seconds" % (duration.days,duration.seconds // 3600,(duration.seconds // 60) % 60,(duration.seconds) % 60)
    return render(request,
        'app/index.html',
        {
            'time_to_finish':duration_str,
            'title':'Home Page',
            'year':datetime.now().year,
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
