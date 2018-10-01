class AI(object):
    """description of class"""

    @staticmethod
    def get_answer(question):
        letters = len(question)
        if(letters == 1):
            return 'There was %s letter in your question' % letters
        else:
            return 'There were %s letters in your question' % letters
