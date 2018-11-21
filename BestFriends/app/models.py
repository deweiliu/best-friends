"""
Definition of models.
"""
import datetime
import pytz

from django.db import models
from app.database.azure_database import AzureDatabase

def birthday(request):
    try:
        username = request.POST['username']
        print(username)
        comment = request.POST['comment']
        print(comment)
        time = "UTC "+str(datetime.datetime.now())[0:19]
        print(time)

        AzureDatabase.insert('BIRTHDAYCOMMENTS',"'" + username + "'","'" + comment + "'","'" + time + "'")


    except:
        print("No comment")

    try:
        records = (AzureDatabase.select('*','BIRTHDAYCOMMENTS'))
        print("records = %s" % (records))
        comments = list()
        for each_record in records:
            comment_dict = dict()
            comment_dict['username'] = each_record[0]
            comment_dict['comment'] = each_record[1]
            comment_dict['datetime'] = each_record[2]
            comments.append(comment_dict)


    except:
        print("Faile to fetch comments")
    return comments


