from django.db import models


class Url(models.Model):
    url = models.URLField()
    short_url = models.URLField()
    password = models.IntegerField()
    clck = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
