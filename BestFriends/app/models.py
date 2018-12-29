"""
Definition of models.
"""
import datetime
from app.bot_service.direct_line_api import DirectLineAPI
from app.variables import Bot
import pytz
from pypika import Query, Table, Field, Order
import time

import random
from django.db import models
from app.database.azure_database import AzureDatabase
def get_user_name(user_id):
    # Get user details
    table = Table('USERS')
    q = Query.from_(table).select('*').where(table.user_id == user_id)
    result = AzureDatabase.execute(str(q))
    first_name = result[0][1]
    surname = result[0][2]
    return (first_name,surname)
def update_conversation_credentials(user_id):
    temporary_key = DirectLineAPI.get_temporary_token(Bot.bot_secret)
    api = DirectLineAPI(user_id,temporary_key)
    api.start_conversation()
    conversationid = api.get_conversationid()
    token = api.get_token()
    watermark='null'
    table=Table('CONVERSATIONS')
    q=Query.from_(table).select('*').where(table.user_id==user_id)
    result=AzureDatabase.execute(str(q))
    if(len(result)==0):
        # no record
        q=Query.into(table).insert(conversationid,user_id,token,watermark)
        AzureDatabase.execute(str(q))

    else:
        q=Query.update(table).set(table.conversation_id,conversationid).where(table.user_id==user_id)
        AzureDatabase.execute(str(q))
        q=Query.update(table).set(table.watermark,watermark).where(table.user_id==user_id)
        AzureDatabase.execute(str(q))
        q=Query.update(table).set(table.token,token).where(table.user_id==user_id)
        AzureDatabase.execute(str(q))


    
def new_user(firstname,surname):
    table = Table('USERS')
    q = Query.from_(table).select('user_id').where(table.firstname == firstname).where(table.surname == surname)
    result = AzureDatabase.execute(str(q))
    print("result = %s" % (result))
    if(len(result) > 0):
        user_id = result[0][0]      #user exist
    else:
        user_id = random.randint(0,1024)        #new user
        q = Query.into(table).insert(user_id,firstname,surname)
        AzureDatabase.execute(str(q))
    return user_id

















def birthday(request):
    table = Table('BIRTHDAYCOMMENTS')

    try:
        username = request.POST['username']
        print(username)
        comment = request.POST['comment']
        print(comment)
        time = "UTC " + str(datetime.datetime.now())[0:19]
        print(time)
        
        q = Query.into(table).insert(username,comment,time)

        AzureDatabase.execute(str(q))
        return None


    except:
        print("No comment")

    try:
        q = Query.from_(table).select('*')
        print(str(q))
        records = (AzureDatabase.execute(str(q)))
        print("records = %s" % (records))
        comments = list()
        for each_record in records:
            comment_dict = dict()
            comment_dict['username'] = each_record[0]
            comment_dict['comment'] = each_record[1]
            comment_dict['datetime'] = each_record[2]
            comments.append(comment_dict)
        return comments


    except Exception as e:
        raise Exception(e.message)
