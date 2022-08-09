from email.headerregistry import Group
from django.contrib import admin
from django.contrib.auth.models import Group

from short_urls.models import Url, ForbiddenDomain

admin.site.register(Url)
admin.site.register(ForbiddenDomain)

admin.site.unregister(Group)
