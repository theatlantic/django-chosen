from django.conf.urls.defaults import patterns, url

from chosen import views

urlpatterns = patterns('',
	url(r'^_static/(?P<path>.*)$', views.static_media, name='chosen-static'),
)