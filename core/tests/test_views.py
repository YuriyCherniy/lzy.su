from django.test import TestCase, Client
from django.shortcuts import reverse


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_index_view_status_code_200(self):
        response = self.c.get(reverse('index-view'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template_used(self):
        response = self.c.get(reverse('index-view'))
        self.assertTemplateUsed(response, 'core/index.html')

    def test_index_view_get_context_data_method(self):
        response = self.c.get(reverse('index-view'))
        text = response.context_data.get('text')
        self.assertTrue(text)
