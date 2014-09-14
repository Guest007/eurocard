from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap
from .models import Article


class HomepageViewSitemap(Sitemap):
    priority = 1
    changefreq = 'monthly'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


class SectionViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['prod', 'makets', 'clients', 'contacts', 'news', 'cards']

    def location(self, item):
        return reverse(item)


class CardsArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Article.objects.filter(category__slug='card', is_active=True)

    def location(self, item):
        return reverse('card', kwargs={'slug': item.slug})


class NewsArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Article.objects.filter(category__slug='news', is_active=True)

    def location(self, item):
        return reverse('newsitem', kwargs={'slug': item.slug})

