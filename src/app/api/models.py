from app.database.azure_database import AzureDatabase
from pypika import Query, Table, Field, Order
from app.bot_service import direct_line_api
import time
def max_message_id(user_id):
    # get the max message id
    table = Table('MESSAGES')
    q = Query.from_(table).select('message_index').where(table.user_id == user_id)
    result = AzureDatabase.execute(str(q))
    max_index = -1
    for each in result:
        index = each[0]
        if(index > max_index):
            max_index = index
    print('max_index= %s' % max_index)
    return max_index

def lodge_message(user_id,message,date_time):
    # Get user details
    table = Table('USERS')
    q = Query.from_(table).select('*').where(table.user_id == user_id)
    result = AzureDatabase.execute(str(q))
    first_name = result[0][1]
    surname = result[0][2]


    currect_index = max_message_id(user_id) + 1

    # add a record
    table = Table('MESSAGES')

    q = Query.into(table).insert(user_id,currect_index,1,first_name,date_time,message)

    result = AzureDatabase.execute(str(q))


    response = dict()
    response['user_id'] = user_id
    response['datetime'] = date_time
    response['username'] = {'first name':first_name,'surname':surname}
    response['message'] = message
    return response

def history_message(user_id):
    table = Table('MESSAGES')
    q = Query.from_(table).select('*').where(table.user_id == user_id)

    result = AzureDatabase.execute(str(q))
    response = list()
    for each_record in result:
        record = dict()
        record['user_id'] = each_record[0]
        record['message_index'] = each_record[1]
        record['is_from_user'] = each_record[2]
        record['sender_name'] = each_record[3]
        record['datetime'] = each_record[4]
        record['message'] = each_record[5]


        response.append(record)
    return response

def get_credentials(user_id):
    table = Table('CONVERSATIONS')
    q = Query.from_(table).select('*').where(table.user_id == user_id)
    result = AzureDatabase.execute(str(q))[0]
    response = dict()
    response['conversation_id'] = result[0]
    response['user_id'] = result[1]
    response['token'] = result[2]
    response['watermark'] = result[3]
    return response

def update_messages(user_id):
    credentials = get_credentials(user_id)
    new_message = direct_line_api.get_new_messages(credentials['conversation_id'],credentials['token'],credentials['user_id'],credentials['watermark'])
    try:
        activities = new_message['activities']
    except:
        activities = list()
    try:
        watermark = new_message['watermark']
    except:
        watermark = 'null'

    # update water mark in database
    table = Table('CONVERSATIONS')

    q = Query.update(table).set(table.watermark,watermark).where(table.user_id == user_id)
    AzureDatabase.execute(str(q))
    # lodge new activities into table "messages"
    table = Table('MESSAGES')

    max_id = max_message_id(user_id)
    
    for each in activities:
        sender_name = each['from']['id']
        if(sender_name != str(user_id)):
            max_id+=1

            is_from_user = 0
            date_time = time.strftime("%Y-%m-%dT%H:%M:%S")
            message = each['text']
            # add a record
            q = Query.into(table).insert(user_id,max_id,is_from_user,sender_name,date_time,message)

            result = AzureDatabase.execute(str(q))
        


def get_new_message(user_id,message_index):
    table = Table('MESSAGES')
    q = Query.from_(table).select('*').where(table.user_id == user_id).where(table.message_index > message_index)
    result = AzureDatabase.execute(str(q))
    
    
    response = list()
    for each_record in result:
        record = dict()
        record['user_id'] = each_record[0]
        record['message_index'] = each_record[1]
        record['is_from_user'] = each_record[2]
        record['sender_name'] = each_record[3]
        record['datetime'] = each_record[4]
        record['message'] = each_record[5]


        response.append(record)
    return response