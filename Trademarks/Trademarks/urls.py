from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from Trademarks import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Trademarks.views.home', name='home'),
    # url(r'^Trademarks/', include('Trademarks.Trademarks.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^search$', views.search, name='search'),
)
