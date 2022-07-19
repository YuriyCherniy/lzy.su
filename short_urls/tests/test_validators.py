from django.test import SimpleTestCase
from django.core.exceptions import ValidationError
from short_urls.validators import LzyURLValidator

class LzyURLValidatorTestCase(SimpleTestCase):

    def setUp(self):
        self.validator = LzyURLValidator()

    def test_domain_lzy_su_is_forbidden(self):
        self.assertRaises(ValidationError, self.validator, 'http://lzy.su')
        self.assertRaises(ValidationError, self.validator, 'https://lzy.su')
        self.assertRaises(ValidationError, self.validator, 'http://www.lzy.su')
        self.assertRaises(ValidationError, self.validator, 'https://www.lzy.su')