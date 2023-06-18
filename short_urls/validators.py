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

        parsed_url = urlparse(value)
        if ForbiddenDomain.objects.filter(
            domain__icontains=parsed_url.netloc
        ).exists():
            raise ValidationError("This link can't be shortened.")
