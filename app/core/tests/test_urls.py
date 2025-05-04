from django.test import SimpleTestCase
from django.urls import resolve, reverse

from core.views import IndexView, TermsOfUseView


class IndexPathTestCase(SimpleTestCase):

    def test_index_view_is_resolved(self):
        url = reverse('index-view')
        view = resolve(url).func.view_class
        self.assertEqual(view, IndexView)


class TermsOfUsePathTestCase(SimpleTestCase):
    def test_terms_of_use_is_resolved(self):
        url = reverse('terms-of-use')
        view = resolve(url).func.view_class
        self.assertEqual(view, TermsOfUseView)
