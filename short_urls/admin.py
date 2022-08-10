from django.contrib import admin
from django.contrib.auth.models import Group

from short_urls.models import ForbiddenDomain, Url

admin.site.register(Url)
admin.site.register(ForbiddenDomain)

admin.site.unregister(Group)
