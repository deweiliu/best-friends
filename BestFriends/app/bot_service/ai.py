from app.bot_service.direct_line_api import DirectLineAPI
from app.variables import V
class AI(object):
    """description of class"""

    @staticmethod
    def get_answer(question):
        temporary_key=DirectLineAPI.get_temporary_token(V.bot_secret)
        api=DirectLineAPI("new user",temporary_key)
        api.start_conversation()
        api.send(question)
        answer= api.receive()
        return answer