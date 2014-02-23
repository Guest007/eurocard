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
    url(r"^uploadfile/", orders.ajax_save, name="uploadfile"),
    url(r"^save/ajax/(?P<step>\d+)/$", orders.save_order, name="ajax-save-order"),

    url(r'^test/', views.test, name='test'),

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
	