from django.views.decorators.csrf import csrf_exempt

"""
Definition of views.
"""
import json
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from BestFriends.settings import prime_number
from BestFriends.settings import compute_gap
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
            'biggest_prime_number':prime_number[0],

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
    """

    HI Kexin
    Check out this founction
    if return a json response instead of an HttpResponse that you should get a dictionary from the response
    """
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
    try:        
        question = request.POST['question']
        answer = AI.get_answer(question)

    except:
        question = 'null'
        answer = 'null'


    # Get a temporary URL for bot service, Following the web page below
    # https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-webchat?view=azure-bot-service-3.0#step-1
    
    # URL for the bot service without password filled
    url_prefix = 'https://webchat.botframework.com/embed/thewaybot?t='
    permanent_secret = 'aq9Rwy7Yd34.cwA.5tk.EFWM7JrOSTrLsNFU5Ivs2c3-gFz_XvXibfr0ihi2PZU'

    # Get the temporary password
    r = requests.get(url = "https://webchat.botframework.com/api/tokens", headers = {'Authorization':'BotConnector %s' % (permanent_secret)}) 
    temporary_token = r.json()
    
    # fill the temporary password into the url
    temporary_secret = url_prefix + temporary_token

    return render(request,
        'app/ai.html',
        {
            'title':'AI',
            #'default_question':'Type your question here',
            'previous_question':'Your question was: %s' % question,
            'previous_answer':'Answer from server: %s' % answer,
            'year':datetime.now().year,
            'temporary_secret':temporary_secret

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
