from django.conf.urls import patterns, url

from homepage import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^search$', views.search, name='search'),
)