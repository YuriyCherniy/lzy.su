from random import randint
from time import time

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


def detect_spam(session, allowed_period=86400, allowed_spam=5):
    '''
    Check the number of short URLs created for allowed period.
    Return True if quantity more then allowed.
    '''
    if not session.get('spam'):
        session['spam'] = 1
        session['spam_date'] = int(time())
    else:
        spam_date = session['spam_date']
        spam_period = int(time()) - spam_date
        if spam_period > allowed_period:
            session['spam_date'] = int(time())
            session['spam'] = 0
        session['spam'] += 1
    return session['spam'] > allowed_spam
