"""
Definition of models.
"""
import datetime
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

def new_user(firstname,surname):
    table = Table('USERS')
    q = Query.from_(table).select('user_id').where(table.firstname == firstname).where(table.surname == surname)
    result = AzureDatabase.execute(str(q))
    print("result = %s" % (result))
    if(len(result) > 0):
        user_id = result[0][0]
    else:
        user_id = random.randint(0,1024)
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
