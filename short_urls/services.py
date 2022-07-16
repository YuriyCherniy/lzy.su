from random import randint

from short_urls.hashids import Hashids
from short_urls.models import Url

hashids = Hashids()


def create_url_object(long_url, request):
    """Genirate a short url identifier and create Url object"""

    # genirate pk for first object in a new db
    try:
        pk_for_hash = Url.objects.last().pk + 1
    except AttributeError:
        pk_for_hash = 1

    short_url = hashids.encode(pk_for_hash)
    url_obj = Url.objects.create(
        long_url=long_url,
        short_url=short_url,
        password=randint(10000, 99999),
        user_ip=request.META.get('HTTP_X_REAL_IP', '0.0.0.0')
    )
    return url_obj
