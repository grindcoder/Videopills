# -*- coding: utf-8 -*-
from django.views.generic.base import RedirectView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from openshift import settings
import video_manager.views
urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', video_manager.views.home),
    url(r'^$',RedirectView.as_view(url='/home', permanent = False) , name = 'Index'),
    url(r'^search/',video_manager.views.search),
)

# include static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# include static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)