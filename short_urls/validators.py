import re

from django.core.validators import URLValidator, ValidationError


class LzyURLValidator(URLValidator):
    """Forbid domain lzy.su for making short URL"""

    def __call__(self, value):
        validator = super().__call__(value)

        forbidden_domain = re.search(r'http[s]{0,1}://lzy.su', value)
        if forbidden_domain:
            raise ValidationError("This link can't be shortened.")

        return validator
