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
def login(request):
    assert isinstance(request, HttpRequest)
    try:
        username = request.POST['username']
        return HttpResponseRedirect(reverse('app:ai',args=(username,)))
    except:
        return render(request,'app/login.html')
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
def ai(request,username):
    print("username = %s",username)
    assert isinstance(request, HttpRequest)    
    return render(request,
        'app/ai.html',
        {
            'title':'AI',
            'year':datetime.now().year,
            'username':username,
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
