from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class IndexSiteMap(Sitemap):

    def items(self):
        return ['index-view']

    def location(self, item):
        return reverse(item)
