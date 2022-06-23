from random import randint

from short_urls.models import Url
from short_urls.hashids import Hashids


hashids = Hashids()


def create_url_object(long_url):
    """Genirate a short url identifier and create Url object"""

    short_url = hashids.encode(Url.objects.last().pk + 1)
    url_obj = Url.objects.create(
        long_url=long_url,
        short_url=short_url,
        password=randint(10000, 99999)
    )
    return url_obj
