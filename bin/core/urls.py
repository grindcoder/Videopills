# -*- coding: utf-8 -*-
from django.views.generic.base import RedirectView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from core import settings
import video_manager.views


urlpatterns = patterns('',
    url(r'^login/$', video_manager.views.user_login, name='login'),
    url(r'^logout/$', video_manager.views.user_logout, name='logout'),
    url(r'^register/$', video_manager.views.register, name='register'),
    # (r'^register/$', 'django.contrib.auth.views.login', {
    # 'template_name': 'Authentication/register_page.html'}),
    # url(r'^register/', video_manager.views.register),
    url(r'^home/', video_manager.views.home),
    url(r'^$',RedirectView.as_view(url='/home', permanent = False) , name = 'Index'),
    url(r'^search/',video_manager.views.search),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test-mail/', video_manager.views.test_mail)
)

# include static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# include static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'video_manager.views.server_error'