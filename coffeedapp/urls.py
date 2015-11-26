from django.conf.urls import patterns, include, urls
from django.contrib import admin
#import core.views as coreviews

urlpatterns = patterns('',

 url(r'^admin/', include(admin.site.urls)), 
 (r'', include('core.urls')),
)

