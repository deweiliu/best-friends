from app.database.azure_database import AzureDatabase
from pypika import Query, Table, Field, Order
def lodge_message(user_id,message,date_time):
    # Get user details
    table = Table('USERS')
    q = Query.from_(table).select('*').where(table.user_id == user_id)
    result = AzureDatabase.execute(str(q))
    first_name = result[0][1]
    surname = result[0][2]


    # get the max message id
    table = Table('MESSAGES')
    q = Query.from_(table).select('message_index').where(table.user_id == user_id)
    result = AzureDatabase.execute(str(q))
    max_index = -1
    for each in result:
        index = each[0]
        if(index > max_index):
            max_index = index
    currect_index = max_index + 1
    print('currect_index= %s' % currect_index)

    # add a record
    q = Query.into(table).insert(user_id,currect_index,1,first_name,date_time,message)

    result = AzureDatabase.execute(str(q))


    response = dict()
    response['user_id'] = user_id
    response['datetime'] = date_time
    response['username'] = {'first name':first_name,'surname':surname}
    response['message'] = message
    return response

def history_message(user_id):
    table=Table('MESSAGES')
    q=Query.from_(table).select('*').where(table.user_id == user_id)

    result = AzureDatabase.execute(str(q))
    response=list()
    for each_record in result:
        record=dict()
        record['user_id']=each_record[0]
        record['message_index']=each_record[1]
        record['is_from_user']=each_record[2]
        record['sender_name']=each_record[3]
        record['datetime']=each_record[4]
        record['message']=each_record[5]


        response.append(record)
    return response