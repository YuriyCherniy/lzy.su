from django.db import models


class Url(models.Model):
    long_url = models.URLField(max_length=2048)
    short_url = models.URLField()
    password = models.IntegerField()
    click = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.long_url
