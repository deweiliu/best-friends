# https://docs.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-direct-line-3-0-concepts?view=azure-bot-service-4.0
# Intergrate with Bot Framework via Direct Line API 3.0
import requests
class DirectLineAPI(object):
    @staticmethod

    def get_temporary_token(secret):
        URL = 'https://webchat.botframework.com/api/tokens'
        HEADERS = {'Authorization':'BotConnector %s' % (secret)}
        r = requests.get(url = URL,headers=HEADERS)
        response = r.json()
        error_message = {'error': {'code': 'BadArgument', 'message': 'Invalid token or secret'}}
        if(response == error_message):
            return None
        else:
            return response
    def start_conversation(self):
        URL = 'https://directline.botframework.com/v3/directline/conversations'
        HEADERS = {"Authorization":"Bearer %s" % self.temporary_token}
        r = requests.post(url=URL,headers=HEADERS)
        if(r.status_code == 201):
            # Connection established
            data = r.json()
            self.conversationId = data['conversationId']
            self.token = data['token']

            return True
        else:
            return False

    def __init__(self, username, temporary_token):
        self.temporary_token = temporary_token
        self.username = username
    def send(self,message):

        URL = 'https://directline.botframework.com/v3/directline/conversations/%s/activities' % (self.conversationId)
        HEADERS = {"Authorization":"Bearer %s" % self.token,'Content-Type': 'application/json'}
        params = {
            "type": "message",
            "from": {
                "id": self.username
            },
            "text": message
        }
        r = requests.post(url=URL,headers=HEADERS,json=params)
        response = r.json()
        if(r.status_code == 200):
            # Message sent successfully
            self.message_id = DirectLineAPI.get_activity_id(response)
            return True
        else:
            # return error message
            return response


    def receive(self):
      URL = 'https://directline.botframework.com/v3/directline/conversations/%s/activities' % (self.conversationId)
      HEADERS = {"Authorization":"Bearer %s" % self.token}

      r = requests.get(url=URL,headers=HEADERS)
      data = (r.json())
      activities = data['activities']
      for each in activities:
        if(DirectLineAPI.get_activity_id(each) > self.message_id):
            return each['text']

    def end_conversation(self):
        URL = 'https://directline.botframework.com/v3/directline/conversations/%s/activities' % (self.conversationId)
        HEADERS = {"Authorization":"Bearer %s" % self.token}
        params = {
    "type": "endOfConversation",
    "from": {
        "id": self.username
    }
}
        r = requests.post(url=URL,headers=HEADERS,json=params)
        if(r.status_code == 200):
            return True
        else:
            return False

 
    @staticmethod
    def get_activity_id(activity):
        id_str = activity['id']
        id_num = id_str.split('|')[1]
        return int(id_num)

