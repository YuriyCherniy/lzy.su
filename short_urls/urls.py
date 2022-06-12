from django.urls import path

from short_urls.views import UrlCreate


urlpatterns = [
    path('', UrlCreate.as_view()),
]
