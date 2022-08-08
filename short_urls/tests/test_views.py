from django.test import Client, TestCase
from django.urls import reverse

from short_urls.models import Url
from short_urls.views import UrlOpen


class ShortUrlViewTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    @classmethod
    def setUpTestData(cls):
        Url.objects.create(long_url='http://site.ru', short_url_hash='hf6', password=0000, user_ip='0.0.0.0')

    # status code 200 tests
    def test_url_cuccess_create_view_status_code_200(self):
        response = self.c.get(reverse('url-create-success'))
        self.assertEqual(response.status_code, 200)

    def test_url_create_view_status_code_200(self):
        response = self.c.get('/https://test-site.com', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_url_create_by_form_view_status_code_200(self):
        response = self.c.post(reverse('url-create-by-form'))
        self.assertEqual(response.status_code, 200)

    # this test does not work in django 3.2 properly
    # def test_url_open_view_status_code_200(self):
    #     url_obj = Url.objects.first()
    #     print(reverse('url-open', args=[url_obj.short_url_hash]))
    #     response = self.c.get(reverse('url-open', args=[url_obj.short_url_hash]), follow=True)
    #     self.assertEqual(response.status_code, 200)

    def test_url_information_view_status_code_200(self):
        url_obj = Url.objects.first()
        response = self.c.get(
            reverse(
                'url-information', kwargs={'short_url_hash': url_obj.short_url_hash, 'password': url_obj.password})
            )
        self.assertEqual(response.status_code, 200)

    def test_url_delete_view_status_code_200(self):
        url_obj = Url.objects.first()
        response = self.c.get(
            reverse(
                'url-information', kwargs={'short_url_hash': url_obj.short_url_hash, 'password': url_obj.password})
            )
        self.assertEqual(response.status_code, 200)

    # status code 302 tests
    def test_url_create_view_status_code_302(self):
        response = self.c.get('/https://test-site.com')
        self.assertEqual(response.status_code, 302)

    def test_url_create_by_form_view_status_code_302(self):
        response = self.c.post(
            reverse('url-create-by-form'), {'long_url': 'https://test-site.com'}
        )
        self.assertEqual(response.status_code, 302)

    def test_url_open_view_status_code_302(self):
        url_obj = Url.objects.first()
        response = self.c.get(reverse('url-open', args=[url_obj.short_url_hash]))
        self.assertEqual(response.status_code, 302)

    # template used tests
    def test_url_create_success_view_template_used(self):
        response = self.c.get(reverse('url-create-success'))
        self.assertTemplateUsed(response, 'short_urls/url_create_success.html')

    def test_url_create_view_success_redirect_template_used(self):
        response = self.c.get('/https://test-site.com', follow=True)
        self.assertTemplateUsed(response, 'short_urls/url_create_success.html')

    def test_url_create_view_error_template_used(self):
        response = self.c.get('/https://test-site-com')
        self.assertTemplateUsed(response, 'short_urls/url_create_error.html')

    def test_url_create_by_form_view_valid_data_template_used(self):
        response = self.c.post(reverse('url-create-by-form'), {'long_url': 'https://test-site.com'}, follow=True)
        self.assertTemplateUsed(response, 'short_urls/url_create_success.html')

    def test_url_create_by_form_view_invalid_data_template_used(self):
        response = self.c.post(reverse('url-create-by-form'), {'long_url': 'https://test-site-com'})
        self.assertTemplateUsed(response, 'core/index.html')

    def test_url_information_view_password_is_correct_template_used(self):
        url_obj = Url.objects.first()
        response = self.c.get(reverse(
            'url-information', kwargs={'short_url_hash': url_obj.short_url_hash, 'password': url_obj.password}
        ))
        self.assertTemplateUsed(response, 'short_urls/url_information.html')

    def test_url_information_view_password_is_not_correct_template_used(self):
        url_obj = Url.objects.first()
        response = self.c.get(reverse(
            'url-information', kwargs={'short_url_hash': url_obj.short_url_hash, 'password': 1234}
        ))
        self.assertTemplateUsed(response, 'short_urls/url_password_error.html')

    def test_url_delete_view_password_is_correct_template_used(self):
        url_obj = Url.objects.first()
        response = self.c.get(reverse(
            'url-delete', kwargs={'short_url_hash': url_obj.short_url_hash, 'password': url_obj.password}
        ))
        self.assertTemplateUsed(response, 'short_urls/url_delete.html')

    def test_url_delete_view_password_is_not_correct_template_used(self):
        url_obj = Url.objects.first()
        response = self.c.get(reverse(
            'url-delete', kwargs={'short_url_hash': url_obj.short_url_hash, 'password': 1234}
        ))
        self.assertTemplateUsed(response, 'short_urls/url_password_error.html')

    # other tests
    def test_url_create_success_view_context_data_is_correct_passed_from_url_create_view(self):
        response = self.c.get('/https://test-site.com', follow=True)
        url_obj = Url.objects.get(long_url='https://test-site.com')
        self.assertEqual(response.context.get('long_url'), url_obj.long_url)
        self.assertEqual(response.context.get('short_url_hash'), url_obj.short_url_hash)
        self.assertEqual(response.context.get('password'), url_obj.password)

    def test_url_create_success_view_context_data_is_correct_passed_from_url_create_by_form_view(self):
        response = self.c.post(
            reverse('url-create-by-form'), {'long_url': 'https://test-site-another.com'}, follow=True
        )
        url_obj = Url.objects.get(long_url='https://test-site-another.com')
        self.assertEqual(response.context.get('long_url'), url_obj.long_url)
        self.assertEqual(response.context.get('short_url_hash'), url_obj.short_url_hash)
        self.assertEqual(response.context.get('password'), url_obj.password)

    def test_open_url_view_get_method_click_counter_works(self):
        url_open_view = UrlOpen()
        url_open_view.get(request=None, short_url_hash='hf6')
        url_obj = Url.objects.get(short_url_hash='hf6')
        self.assertEqual(url_obj.clicks, 1)

    def test_url_information_view_get_context_data_method(self):
        url_obj = Url.objects.get(short_url_hash='hf6')
        response = self.c.get(
            reverse('url-information', kwargs={'short_url_hash': 'hf6', 'password': 0000})
        )
        self.assertEqual(response.context_data.get('url_clicks'), url_obj.clicks)
        self.assertEqual(response.context_data.get('long_url'), url_obj.long_url)
        self.assertEqual(response.context_data.get('url_created'), url_obj.created)

    def test_url_delete_view_get_method(self):
        url_obj = Url.objects.last()
        self.c.get(
            reverse('url-delete', kwargs={
                'short_url_hash': url_obj.short_url_hash, 'password': url_obj.password
            })
        )
        url_obj.refresh_from_db()

    def test_url_create_view_object_created(self):
        self.c.get('/https://test-site.com')
        self.assertEqual(Url.objects.count(), 2)

    def test_url_create_view_object_not_created_domain_lzy_su_is_forbidden(self):
        self.c.get('/https://lzy.su')
        self.assertEqual(Url.objects.count(), 1)

    def test_url_create_by_form_view_object_created(self):
        self.c.post(reverse('url-create-by-form'), {'long_url': 'https://test-site.com'})
        self.assertEqual(Url.objects.count(), 2)

    def test_url_create_by_form_view_object_not_created_domain_lzy_su_is_forbidden(self):
        self.c.post(reverse('url-create-by-form'), {'long_url': 'https://lzy.su'})
        self.assertEqual(Url.objects.count(), 1)