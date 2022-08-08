from random import randint

from short_urls.hashids import Hashids
from short_urls.models import Url

hashids = Hashids()


def create_url_object(long_url, request):
    url_obj = Url.objects.create(
        long_url=long_url,
        short_url='',  # generate a short url identifier will be performed in the next step
        password=randint(10000, 99999),
        user_ip=request.META.get('HTTP_X_REAL_IP', '0.0.0.0')
    )
    # generate the short url identifier and save object to db
    url_obj.short_url = hashids.encode(url_obj.pk)
    url_obj.save(update_fields=['short_url'])
    return url_obj
