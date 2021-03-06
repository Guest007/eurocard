from django.conf.urls import patterns, include, url

from eurocard import settings
from articles import views
from orders import views as orders

from django.conf.urls.static import static
from django.contrib import admin
import grappelli
from filebrowser.sites import site
from orders.views import save_order
# from django.views.generic.simple import direct_to_template
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from rollyourown.seo.admin import register_seo_admin
from django.contrib import admin
from articles.seo import EuroCardMetadata

register_seo_admin(admin.site, EuroCardMetadata)
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^prod/$', views.prod, name='prod'),
    #url(r'^clients/$', views.clients, name='clients'),
    #url(r'^article/(?P<slug>[\S\-]+?)/$', views.newsitem, name='newsitem'),

    url(r'^news/(?P<slug>[\S\-]+?)/$', views.newsitem, name='newsitem'),
    url(r'^news/$', views.news, name='news'),
    #url(r'^cards/', views.cards, name='cards'),
    url(r'^cards/(?P<slug>[\S\-]+?)/$', views.card, name='card'),
    url(r'^cards/$', views.cards, name='cards'),

    url(r'^price/$', views.price, name='price'),
    url(r'^makets/$', views.makets, name='makets'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^page/(?P<slug>[\S\-]+?)/$', views.pages, name='page'),

    # Ajax actions
    url(r'^form_2/', orders.fastform, name='f_order'),
    url(r'^form_1/', orders.easyform, name='e_order'),
    url(r'^form_3/', orders.readyform, name='r_order'),
    url(r'^call-back/', orders.callback, name='call-back'),
    url(r'^finish/', orders.finish, name='finish'),

    url(r"^second/(?P<pk>\d+)/$", orders.nextstep_order, name="ajax-nextstep-order"),
    url(r"^(?P<pk>\d+)/(?P<step>\d+)/$", orders.edit_fast, name="edit-fast"),
    url(r"^(?P<pk>\d+)/$", orders.edit_fast, name="edit-fast"),
    url(r"^(?P<pk>\d+)/(?P<step>\d+)/$", orders.edit_easy, name="edit-easy"),
    url(r"^(?P<pk>\d+)/$", orders.edit_easy, name="edit-easy"),
    url(r"^(?P<pk>\d+)/(?P<step>\d+)/$", orders.edit_templ, name="edit-templ"),
    url(r"^(?P<pk>\d+)/$", orders.edit_templ, name="edit-templ"),
    url(r"^uploadfile/", orders.ajax_save, name="uploadfile"),
    url(r"^save/ajax/(?P<step>\d+)/$", orders.save_order, name="ajax-save-order"),
    url(r"^save/templ/(?P<step>\d+)/$", orders.save_order1, name="ajax-save-torder"),

    url('^yandex_525028000777872e.html', TemplateView.as_view(template_name='yandex_525028000777872e.html')),
    url('^robots.txt', TemplateView.as_view(template_name='robots.txt')),
    #url('^sitemap.xml', TemplateView.as_view(template_name='sitemap.xml')),
    #url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

# sitemap.xml
from django.contrib.sitemaps import views as sitemaps_views

from articles.sitemaps import (HomepageViewSitemap, SectionViewSitemap,
        CardsArticleSitemap, NewsArticleSitemap)

sitemaps = {
    'homepage': HomepageViewSitemap,
    'sections': SectionViewSitemap,
    'cards': CardsArticleSitemap,
    'news': NewsArticleSitemap,
}

urlpatterns += patterns('',
    url(r'^sitemap\.xml$', sitemaps_views.sitemap,
        {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    #url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps}),
    #url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap, {'sitemaps': sitemaps}),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
