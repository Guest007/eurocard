from django.conf.urls import patterns, include, url

from eurocard import settings
from articles import views

from django.conf.urls.static import static
from django.contrib import admin
import grappelli
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^prod/', views.prod, name='prod'),
    url(r'^clients/', views.clients, name='clients'),
    url(r'^article/(?P<slug>[\S\-]+?)/$', views.newsitem, name='newsitem'),
    url(r'^news/', views.news, name='news'),
    url(r'^about/', views.about, name='about'),
    url(r'^price/', views.price, name='price'),
    url(r'^cooperation/', views.cooperation, name='cooperation'),
    url(r'^contacts/', views.contacts, name='contacts'),


    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)