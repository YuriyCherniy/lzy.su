from random import randint

from django.views import View
from django.core.validators import URLValidator, ValidationError
from django.shortcuts import render

from short_urls.models import Url
from short_urls.hashids import Hashids


hashids = Hashids()
validate_url = URLValidator()


class UrlCreate(View):
    def get(self, request, **kwargs):
        url = kwargs.get('url', '')
        try:
            validate_url(url)
            short_url = hashids.encode(Url.objects.count() + 1)
            url = Url.objects.create(
                url=url,
                short_url=short_url,
                password=randint(10000, 99999)
            )
        except ValidationError:
            return render(request, 'short_urls/url_create_error.html')
        return render(request, 'short_urls/url_create.html', {'url': url})
