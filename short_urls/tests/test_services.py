from django.test import SimpleTestCase

from short_urls.services import detect_spam


class ServicesTestCase(SimpleTestCase):
    def test_detect_spam_function(self):
        self.assertEqual(detect_spam({'spam': 4}), False)
        self.assertEqual(detect_spam({'spam': 5}), True)
