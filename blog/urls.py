from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.detail_article, name='article')
]