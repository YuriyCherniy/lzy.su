from django.db import models


class Url(models.Model):
    long_url = models.URLField(max_length=2048)
    short_url_hash = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    clicks_per_day = models.IntegerField(default=0)  # not implemented yet
    clicks = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    user_ip = models.GenericIPAddressField(unpack_ipv4=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[ {self.long_url[:40]} ] from ip [{self.user_ip}]'


class ForbiddenDomain(models.Model):
    domain = models.CharField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[ {self.domain} ] created: {self.created.date()}'