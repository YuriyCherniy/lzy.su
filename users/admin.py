from django.contrib import admin

from users.models import LazyUser


admin.site.register(LazyUser)
