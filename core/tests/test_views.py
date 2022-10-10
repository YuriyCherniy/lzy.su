from django.shortcuts import reverse
from django.test import Client, TestCase, SimpleTestCase


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


class TermsOfUseTestCase(SimpleTestCase):

    def setUp(self):
        self.c = Client()

    def test_terms_of_use_view_status_code_200(self):
        response = self.c.get(reverse('terms-of-use'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template_used(self):
        response = self.c.get(reverse('terms-of-use'))
        self.assertTemplateUsed(response, 'core/terms_of_use.html')