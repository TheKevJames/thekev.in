from django.conf.urls import patterns, url
from web.views import *


urlpatterns = patterns('',
	url(r'^$', home),
	url(r'^timeline$', timeline),
	url(r'^resource$', resource),
	(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
)
