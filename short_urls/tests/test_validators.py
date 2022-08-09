from django.core.exceptions import ValidationError
from django.test import TestCase

from short_urls.models import ForbiddenDomain
from short_urls.validators import LzyURLValidator


class LzyURLValidatorTestCase(TestCase):

    def setUp(self):
        self.validator = LzyURLValidator()
        ForbiddenDomain.objects.create(domain='lzy.su')
        ForbiddenDomain.objects.create(domain='www.lzy.su')


    def test_domain_lzy_su_is_forbidden(self):
        self.assertRaises(ValidationError, self.validator, 'http://lzy.su')
        self.assertRaises(ValidationError, self.validator, 'https://www.lzy.su')