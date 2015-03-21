from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from openshift import settings
import video_manager.views
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', video_manager.views.redirect_to_videopills)
)

# include static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
