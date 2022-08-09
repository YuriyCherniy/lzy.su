from random import randint

from django.contrib.auth.hashers import make_password
from hashids import Hashids

from short_urls.models import Url

hashids = Hashids()


def create_url_object(long_url, request):
    raw_password = str(randint(10000, 99999))
    url_obj = Url.objects.create(
        long_url=long_url,
        short_url_hash='',  # generating a short url identifier will be performed in the next step
        password=make_password(raw_password),
        user_ip=request.META.get('HTTP_X_REAL_IP', '0.0.0.0')
    )
    # generate the short url identifier and save object to db
    url_obj.short_url_hash = hashids.encode(url_obj.pk)
    url_obj.save(update_fields=['short_url_hash'])
    return url_obj, raw_password
