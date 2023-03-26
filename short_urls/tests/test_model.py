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
        obj = ForbiddenDomain.objects.get(domain='lzy.su')
        self.assertEqual(obj.__str__(), f'[ {obj.domain} ] created: {obj.created.date()}')
