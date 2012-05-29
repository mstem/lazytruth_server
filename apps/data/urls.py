from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
	url(r'^api/%s/match/?' % settings.API_VERSION, 'apps.data.views.match'),
	url(r'^test/?', 'apps.data.views.test'),
	url(r'^mirror/?', 'apps.data.views.post_mirror'),
    #	url(r'^submit/', include(admin.site.urls)),
)

