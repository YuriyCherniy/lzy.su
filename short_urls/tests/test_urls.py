from django.test import SimpleTestCase
from django.urls import reverse, resolve

from short_urls.views import UrlCreateByForm, UrlCreateSuccess, UrlOpen, UrlInformation, UrlDelete, UrlCreate


class UrlPathTestCase(SimpleTestCase):
    def test_url_create_view_is_resolved(self):
        url = '/https://some-site.com'
        view = resolve(url).func.view_class
        self.assertEqual(view, UrlCreate)

    def test_url_create_by_html_form_view_is_resolved(self):
        url = reverse('url-create-by-form')
        view = resolve(url).func.view_class
        self.assertEqual(view, UrlCreateByForm)

    def test_url_create_success_view_is_resolved(self):
        url = reverse('url-create-success')
        view = resolve(url).func.view_class
        self.assertEqual(view, UrlCreateSuccess)

    def test_url_open_view_is_resolved(self):
        url = '/Ab1/'
        view = resolve(url).func.view_class
        self.assertEqual(view, UrlOpen)

    def test_url_information_view_is_resolved(self):
        url = '/Ab1/i/12345/'
        view = resolve(url).func.view_class
        self.assertEqual(view, UrlInformation)

    def test_url_delete_view_is_resolved(self):
        url = '/Ab1/d/12345/'
        view = resolve(url).func.view_class
        self.assertEqual(view, UrlDelete)
