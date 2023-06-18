from tracemalloc import DomainFilter

from django.test import TestCase

from short_urls.models import ForbiddenDomain, Url


class UrlModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Url.objects.create(
            long_url='http://test.ru/some-long-url-from-the-internet',
            short_url_hash='test',
            password=00000,
            is_lazy=False,
        )

        ForbiddenDomain.objects.create(domain='lzy.su')

    def test_url_model_str_method(self):
        url_obj = Url.objects.get(short_url_hash='test')
        self.assertEqual(
            url_obj.__str__(), f'[ http://test.ru/some-long-url-from-the-in ] created at [{url_obj.created}]'
        )

    def test_forbidden_domain_str_method(self):
        obj = ForbiddenDomain.objects.get(domain='www.lzy.su')
        self.assertEqual(obj.__str__(), f'[ {obj.domain} ] created: {obj.created.date()}, already exist 0')

    def test_forbidden_domain_str_method_exist_two_forbidden_domain(self):
        Url.objects.create(
            long_url='http://www.lzy.su/some-long-url-from-the-internet',
            short_url_hash='test_2',
            password=00000,
            is_lazy=False,
        )
        Url.objects.create(
            long_url='http://lzy.su/some-long-url-from-the-internet',
            short_url_hash='test_2',
            password=00000,
            is_lazy=False,
        )
        obj = ForbiddenDomain.objects.get(domain='www.lzy.su')
        self.assertEqual(obj.__str__(), f'[ {obj.domain} ] created: {obj.created.date()}, already exist 2')

    def test_forbidden_domain_save_method(self):
        obj_https_www = ForbiddenDomain.objects.create(domain='https://www.youtube.com/')
        obj_https = ForbiddenDomain.objects.create(domain='https://youtube.com/')
        obj_http_www = ForbiddenDomain.objects.create(domain='http://www.youtube.com/')
        obj_http = ForbiddenDomain.objects.create(domain='http://youtube.com/')
        obj_www = ForbiddenDomain.objects.create(domain='www.youtube.com/')
        obj = ForbiddenDomain.objects.create(domain='youtube.com/')
        self.assertEqual(obj_https_www.domain, 'www.youtube.com/')
        self.assertEqual(obj_https.domain, 'www.youtube.com/')
        self.assertEqual(obj_http_www.domain, 'www.youtube.com/')
        self.assertEqual(obj_http.domain, 'www.youtube.com/')
        self.assertEqual(obj_www.domain, 'www.youtube.com/')
        self.assertEqual(obj.domain, 'www.youtube.com/')
