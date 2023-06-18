from urllib.parse import urlparse

from django.core.validators import URLValidator, ValidationError

from short_urls.models import ForbiddenDomain


class ForbiddenDomainValidator(URLValidator):
    """
    Extends standard URLValidator to forbid domains
    from ForbiddenDomain model for making short URLs
    """

    def __call__(self, value):
        super().__call__(value)

        forbidden_domains = [obj.domain for obj in ForbiddenDomain.objects.all()]
        parsed_url = urlparse(value)
        if parsed_url.netloc in forbidden_domains:
            raise ValidationError("This link can't be shortened.")
