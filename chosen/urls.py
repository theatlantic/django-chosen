from django.conf.urls.defaults import patterns, url

from views import static_media


urlpatterns = patterns('',
    url(r'^_static/(?P<path>.*)$', static_media, name='chosen-static'),
)
