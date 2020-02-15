import unittest
from app.variables import Bot
from app.bot_service.direct_line_api import DirectLineAPI


class Test_DirectLineAPITest(unittest.TestCase):
    def test_A(self):
        self.assertEqual(True, True)
        activity = {'id': 'Eoa2KkO3OUq3zyS3n4fiHb|0000002'}
        id = DirectLineAPI.get_activity_id(activity)
        self.assertEqual(2, id)

        activity = {'id': 'HwoYvONWNOd21znBK2F1H3|0000002'}
        id = DirectLineAPI.get_activity_id(activity)
        self.assertEqual(2, id)

    def test_B(self):

        answer = DirectLineAPI.get_temporary_token(Bot.bot_secret)
        self.assertEqual(str, type(answer))

        secret = 'wrong_secret'
        answer = DirectLineAPI.get_temporary_token(secret)
        self.assertEqual(type(None), type(answer))


if __name__ == '__main__':
    unittest.main()
