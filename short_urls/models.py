import re

from django.db import models


class Url(models.Model):
    long_url = models.URLField(max_length=2048)
    short_url_hash = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    clicks_on_short_url = models.IntegerField(default=0)
    clicks_on_long_url = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_lazy = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[ {self.long_url[:40]} ] created at [{self.created}]'


class ForbiddenDomain(models.Model):
    domain = models.URLField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        '''
        Prepare domain name for ForbiddenDomainValidator
        '''
        domain = re.sub(r'http[s]{0,1}://', '', self.domain, 1)
        if domain.startswith('www.'):
            self.domain = domain
        else:
            self.domain = f'www.{domain}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'[ {self.domain} ] created: {self.created.date()}'
