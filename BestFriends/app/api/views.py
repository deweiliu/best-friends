import json
import requests
from django.http import HttpResponse
from django.http import HttpRequest
from datetime import datetime
from app import models
from app.bot_service.ai import AI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def api(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    post = None
    if(request.method == 'POST'):
        # post request for uploading a message and store it into database
        post = True
    elif(request.method == 'GET'):
        # get request for fetching data from data base
        post = False
    else:
        raise Exception("The request is neither 'POST' nor 'GET'")

    # load json data
    # Get the body request
    body = (request.body)
        
    # Decode the request into a str object then parse it to a dictionary
    data = json.loads(body.decode("ascii"))
    

    if(post):
        return post_api(data)
    else:
        return get_api(data)
        
def post_api(data):
    try:
        type = data['type']
    except:
        return JsonResponse({'error':'request body must have a key "type"'},status=400)

    if(type == 'send message'):
        return send_message(data)
    else:
        return JsonResponse({'error':'invalid "type" in the POST request'},status=400)
    return JsonResponse({"answer_dict_name":'hi'})
def get_api(data):
    try:
        type = data['type']
    except:
        return JsonResponse({'error':'request body must have a key "type"'},status=400)

    if(type == 'history messages'):
        return history_message(data)
    elif(type == 'message update'):
        return message_update(data)
    else:
        return JsonResponse({'error':'invalid "type" in the GET request'},status=400)

def history_message(data):
    return JsonResponse({'message':'from history_message'},status=200)
def send_message(data):
    return JsonResponse({'message':'from send message'},status=200)
def message_update(data):
    return JsonResponse({'message':'from message_update'},status=200)
