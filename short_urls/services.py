from random import randint

from django.contrib.auth.hashers import make_password
from hashids import Hashids

from short_urls.models import Url

hashids = Hashids()


def create_url_object(long_url, is_spam, is_lazy=False):
    """
    Generate password to manage an object and create the object
    """
    raw_password = str(randint(10000, 99999))
    url_obj = Url.objects.create(
        long_url=long_url,
        short_url_hash='',  # generating a short url identifier will be performed on the next step
        password=make_password(raw_password),
        is_lazy=is_lazy,
        is_spam=is_spam,
    )
    url_obj.short_url_hash = hashids.encode(url_obj.pk)  # generate the short url identifier
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


def detect_spam(session):
    '''
    Check the number of short URLs generated per session.
    Return True if quantity more then allowed.
    '''
    if not session.get('spam'):
        session['spam'] = 1
    else:
        session['spam'] += 1
    return session['spam'] > 5
