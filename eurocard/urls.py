from django.conf.urls import patterns, include, url

from eurocard import settings
from articles import views
from orders import views as orders

from django.conf.urls.static import static
from django.contrib import admin
import grappelli
from filebrowser.sites import site
from orders.views import save_order

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
    url(r'^test/', orders.home, name='t_order'),
    # Ajax actions
    url(r"^second/(?P<pk>\d+)/$", orders.nextstep_order, name="ajax-nextstep-order"),
    url(r"^(?P<pk>\d+)/(?P<step>\d+)/$", orders.edit_order, name="edit-order"),
    url(r"^(?P<pk>\d+)/$", orders.edit_order, name="edit-order"),
    url(r"^save/ajax/(?P<step>\d+)/$", orders.save_order, name="ajax-save-order"),


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