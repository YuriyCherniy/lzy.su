from django.test import TestCase

from short_urls.models import Url


class UrlModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Url.objects.create(
            long_url='http://test.ru/some-long-url-from-the-internet',
            short_url_hash='test',
            password=00000,
            user_ip='0.0.0.0'
        )

    def test_url_model_str_method(self):
        url_obj = Url.objects.get(short_url_hash='test')
        self.assertEqual(
            url_obj.__str__(), '[ http://test.ru/some-long-url-from-the-in ] from ip [0.0.0.0]'
        )
