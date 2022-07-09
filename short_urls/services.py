from random import randint

from short_urls.models import Url
from short_urls.hashids import Hashids


hashids = Hashids()


def create_url_object(long_url):
    """Genirate a short url identifier and create Url object"""

    # genirate pk for first object in new db
    try:
        pk_for_hash = Url.objects.last().pk + 1
    except Url.DoesNotExist:
        pk_for_hash = 1

    short_url = hashids.encode(pk_for_hash)
    url_obj = Url.objects.create(
        long_url=long_url,
        short_url=short_url,
        password=randint(10000, 99999)
    )
    return url_obj
