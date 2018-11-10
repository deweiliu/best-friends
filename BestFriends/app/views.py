from django.views.decorators.csrf import csrf_exempt

"""
Definition of views.
"""
import json
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime

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

def js_ai(request):
    assert isinstance(request, HttpRequest)
    try:
        question = request.GET.get('Twords',0)
        print("question is : %s" % question)
        answer = AI.get_answer(question)
        print("anwser is : %s" % answer)
    except:
        answer = 'Got an exception from views.js_ai'
    answer_dict = {"answer_dict_name":answer}
    return JsonResponse(answer_dict)
   
@csrf_exempt
def conversation(request):
    try:
        # Get the body request
        body = (request.body)
        
        # Decode the request into a str object then parse it to a dictionary
        data = json.loads(body.decode("ascii"))

        question = data['question']
        print("Got question : %s" % question)
        answer = AI.get_answer(question)
    except:
        answer = "Invaild request! The body of the request must be a dictionary containing a key 'question'. but the requestion body we got from you was: %s" % (str(data))
    return JsonResponse({'answer':answer})

@csrf_exempt
def ai(request):
    assert isinstance(request, HttpRequest)    
    return render(request,
        'app/ai.html',
        {
            'title':'AI',
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
def error404(request):
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/404error.html',
        { 
        'title':'404',
        'year':datetime.now().year,

        })
