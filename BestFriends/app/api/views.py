from app.bot_service.direct_line_api import send_message_to_bot
import json
import time
import requests
from django.http import HttpResponse
from django.http import HttpRequest
from datetime import datetime
from app.api import models
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
        return error_response("The request is neither 'POST' nor 'GET'")

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
    method = 'POST'

    try:
        type = data['type']
    except:
        return error_response('request body must have a key "type"',request_method=method)

    if(type == 'send message'):
        return send_message(method,data)
    else:
        return error_response('invalid "type" in the POST request',request_method=method)

def get_api(data):
    method = 'GET'
    try:
        type = data['type']
    except:
        return error_response('request body must have a key "type"',request_method=method)

    if(type == 'history messages'):
        return history_messages(method,data)
    elif(type == 'message update'):
        return message_update(method,data)
    else:
        return JsonResponse({'error':'invalid "type" in the GET request'},status=400)

def history_messages(request_method,data):
    type = 'history messages'
    try:
        user_id = data['user_id']
    except:
        return error_response('Not enough keys in the request',request_method=request_method,type=type)
    
    records = models.history_message(user_id)
    response = dict()
    response['records'] = records
    response['user_id'] = user_id

    return JsonResponse(response,status=200)


def send_message(request_method,data):
    type = 'send message'
    try:
        user_id = data['user_id']
        message = data['message']
    except:
        return error_response('Not enough keys in the request',request_method=request_method,type=type)
    date_time = time.strftime("%Y-%m-%dT%H:%M:%S")
    print('datetime = %s' % date_time)
    response = models.lodge_message(user_id,message,date_time)
    response['response'] = 'Request received'

    credentials = models.get_credentials(user_id)

    result = send_message_to_bot(credentials['conversation_id'],credentials['token'],user_id,message)
    if(result == True):
        print('Message sent successfully')
    else:
        print(result)
        raise Exception('Cannot send message to bot')
    
    
    return JsonResponse(response,status=201)


def message_update(request_method,data):
    type = 'message update'
    try:
        user_id = data['user_id']
        message_index = data['message_index']
    except:
        return error_response('Not enough keys in the request',request_method=request_method,type=type)
    models.update_messages(user_id)
    result = models.get_new_message(user_id,message_index)

    response = dict()
    response['new_messages'] = result
    response['user_id'] = user_id

    return JsonResponse(response,status=200)


def error_response(message,request_method='unknown',type='invalid type'):
    response = dict()
    response['error'] = 'Bad request'
    response['request method'] = request_method
    response['type'] = type
    response['message'] = message
    return JsonResponse(response,status=400)