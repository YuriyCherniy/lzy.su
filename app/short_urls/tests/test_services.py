from time import time

from django.test import SimpleTestCase

from short_urls.services import detect_spam


class ServicesTestCase(SimpleTestCase):
    def test_detect_spam_function(self):
        self.assertEqual(detect_spam({}), False)  # first creation, is not spam
        self.assertEqual(detect_spam({'spam': 4, 'spam_date': int(time())}), False)  # fifth creation, is not spam
        self.assertEqual(detect_spam({'spam': 5, 'spam_date': int(time())}), True)  # sixth creation, is spam

    def test_detect_spam_function_spam_period_expire(self):
        spam_date = int(time()) - 2
        spam = 5
        result = detect_spam({'spam': spam, 'spam_date': spam_date}, allowed_period=1)
        self.assertEqual(result, False)
