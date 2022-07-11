from django.test import SimpleTestCase
from django.urls import resolve, reverse

from core.views import IndexView


class IndexPathTestCase(SimpleTestCase):

    def test_index_view_is_resolved(self):
        url = reverse('index-view')
        view = resolve(url).func.view_class
        self.assertEqual(view, IndexView)
