from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

"""
Definition of views.
"""
import json
import requests
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from datetime import datetime
from app import models
from app.bot_service.ai import AI
from django.http import JsonResponse
from app.api import views as api_views
from app.api import models as api_models


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
                  'app/index.html',
                  {
                      'title': 'Home Page',
                      'year': datetime.now().year,

                  })


def about(request):
    assert isinstance(request, HttpRequest)
    time_value = int(float(os.getenv('UPDATE_TIME', default=0)))
    update_date = datetime.fromtimestamp(time_value).strftime("%A %d %B %Y")
    return render(request,
                  'app/about.html',
                  {
                      'title': 'About',
                      'update_date': update_date,
                      'year': datetime.now().year,
                  })


def login(request):
    assert isinstance(request, HttpRequest)

    try:
        first_name = request.POST['first_name']
        surname = request.POST['surname']
        user_id = models.new_user(first_name, surname)
        r = reverse('app:ai', args=(user_id,))
        return HttpResponseRedirect(r)
    except:
        return render(request,
                      'app/login.html',
                      {
                          'title': 'Login',
                          'year': datetime.now().year,
                      })


@csrf_exempt
def ai(request, user_id):
    models.update_conversation_credentials(user_id)
    username = models.get_user_name(user_id)
    firstname = username[0]
    surname = username[1]

    assert isinstance(request, HttpRequest)

    credentials = api_models.get_credentials(user_id)

    data = {'user_id': user_id, 'message': 'testing message', 'datetime': 'fsdl'}

    print("Sending testing message")
    api_views.send_message('POST', data, True)

    return render(request,
                  'app/ai.html',
                  {
                      'title': 'AI',
                      'year': datetime.now().year,
                      'firstname': firstname,
                      "surname": surname,
                      'user_id': user_id
                  })


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
                  'app/contact.html',
                  {
                      'title': 'Contact',
                      'message': 'Please do not hesitate to contact us with the information below.',
                      'year': datetime.now().year,
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
        output += ("<span>At " + comment['datetime'] +
                   ", " + comment['username'] + " said:</span>")
        output += ("<br /><h3><span>" +
                   comment['comment'] + "</span></h3><br /><br />")

    return render(request,
                  'app/birthday.html',
                  {
                      'title': 'Birthday',
                      'content': '',
                      'year': datetime.now().year,
                      'comments': comments
                  })


def error404(request):
    assert isinstance(request, HttpRequest)
    return render(request,
                  'app/404error.html',
                  {
                      'title': '404',
                      'year': datetime.now().year,

                  })
