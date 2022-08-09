from django.contrib import admin

from short_urls.models import Url, ForbiddenDomain

admin.site.register(Url)
admin.site.register(ForbiddenDomain)
