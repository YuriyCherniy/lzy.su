from django.contrib import admin
from django.contrib.auth.models import Group

from short_urls.models import ForbiddenDomain, Url


class UrlInLine(admin.StackedInline):
    model = Url
    fields = ['is_active']
    verbose_name_plural = 'ALREADY EXISTING LINKS WITH A FORBIDDEN DOMAIN'
    extra = 0
    max_num = 0
    show_change_link = True
    


class AdminForbiddenDomain(admin.ModelAdmin):
    inlines = [UrlInLine]


admin.site.register(Url)
admin.site.register(ForbiddenDomain, AdminForbiddenDomain)

admin.site.unregister(Group)
