from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

"""
Definition of views.
"""
import json
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect
from datetime import datetime
from app import models
from app.bot_service.ai import AI
from django.http import JsonResponse

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,

        })


def login(request):
    assert isinstance(request, HttpRequest)

    try:
        first_name = request.POST['first_name']
        surname = request.POST['surname']
        user_id = models.new_user(first_name,surname)
        r = reverse('app:ai',args=(user_id,))
        return HttpResponseRedirect(r)
    except:
        return render(request,'app/login.html')


@csrf_exempt
def ai(request,user_id):
    models.update_conversation_credentials(user_id)
    username = models.get_user_name(user_id)
    firstname = username[0]
    surname = username[1]


    assert isinstance(request, HttpRequest)
    return render(request,
        'app/ai.html',
        {
            'title':'AI',
            'year':datetime.now().year,
            'firstname':firstname,
            "surname":surname,
            'user_id':user_id
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

def birthday(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    comments = models.birthday(request)
    if(comments == None):
        return HttpResponseRedirect(reverse('app:birthday'))

    output = ''
    print(comments)
    for comment in comments:
        output+=("<span>At " + comment['datetime'] + ", " + comment['username'] + " said:</span>")
        output+=("<br /><h3><span>" + comment['comment'] + "</span></h3><br /><br />")

    return render(request,
        'app/birthday.html',
        {
            'title':'About',
            'message':'This project is being developed by Kexin Huang & Dewei Liu who are the best friends in the world, since 14 Aug 2018!',
            'content':'',
            'year':datetime.now().year,
            'comments':comments
        })
def error404(request):
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/404error.html',
        { 
        'title':'404',
        'year':datetime.now().year,

        })
