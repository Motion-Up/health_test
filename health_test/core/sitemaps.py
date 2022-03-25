from django.contrib.sitemaps import Sitemap
from tests.models import Test


class TestSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Test.objects.all()

    def location(self, obj):
        return '/viewoutside.ru/test/%s' % (obj.slug)
