from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.sitemaps.views import sitemap

from core.views import RobotsTxt
from core.sitemap import IndexSiteMap
from short_urls.views import (UrlCreate, UrlCreateByForm, UrlCreateSuccess,
                              UrlDelete, UrlInformation, UrlOpen)

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path(f'{settings.SECRET_ADMIN_URL}/', admin.site.urls),
    path('', include('core.urls')),
    re_path(
        r"^(?P<url>http[s]{0,1}://[[\]A-Za-zА-Яа-я0-9-._~:/?#@!$&'()*+,;=]{,2000})$",
        UrlCreate.as_view()
    ),
    path('create/', UrlCreateByForm.as_view(), name='url-create-by-form'),
    path('success/', UrlCreateSuccess.as_view(), name='url-create-success'),
    path('<str:short_url>/', UrlOpen.as_view(), name='url-open'),
    path('<str:short_url>/i/<int:password>/', UrlInformation.as_view(), name='url-information'),
    path('<str:short_url>/d/<int:password>/', UrlDelete.as_view(), name='url-delete'),
    path('robots.txt', RobotsTxt.as_view()),
    path(
        'sitemap.xml', sitemap, {'sitemaps': {'index-view': IndexSiteMap()}},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]
