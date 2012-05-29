from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings 


admin.autodiscover()

urlpatterns = patterns('',
	url(r'^data/', include('apps.data.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

print settings.MEDIA_URL,settings.STATIC_URL

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
