import re

from django.core.validators import URLValidator, ValidationError


class LzyURLValidator(URLValidator):
    """Forbid domain lzy.su for making short URL"""

    def __call__(self, value):
        super().__call__(value)

        regexp = r'http[s]{0,1}://[w]{0,1}[w]{0,1}[w]{0,1}[\.]{0,1}lzy\.su'
        forbidden_domain = re.search(regexp, value)
        if forbidden_domain:
            raise ValidationError("This link can't be shortened.")
