from random import randint

from django.contrib.auth.hashers import make_password
from hashids import Hashids

from short_urls.models import Url

hashids = Hashids()


def create_url_object(long_url, is_lazy=False):
    """
    Generate password to manage an object and create the object

    :param long_url: a string captured from browser's address bar or HTML form.
    :param is_lazy: a boolean represents which way a user requested to create Url object.
    If the user created a short URL by typing a command in browser's address bar, is_lazy=True
    otherwise is_lazy=False.
    :return: the Url object and raw password
    """
    raw_password = str(randint(10000, 99999))
    url_obj = Url.objects.create(
        long_url=long_url,
        short_url_hash='',  # generating a short url identifier will be performed on the next step
        password=make_password(raw_password),
        is_lazy=is_lazy,
    )
    # generate the short url identifier and save object to db
    url_obj.short_url_hash = hashids.encode(url_obj.pk)
    url_obj.save(update_fields=['short_url_hash'])
    return url_obj, raw_password


def prepare_session(session, url_obj, raw_password):
    '''
    Prepare session to pass dict to UrlCreateSuccess view for context data
    '''
    session.update({
        'short_url_hash': url_obj.short_url_hash,
        'raw_password': raw_password
    })
