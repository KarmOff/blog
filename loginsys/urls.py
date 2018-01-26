from django.conf.urls import include, url
from loginsys import views

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^registration/$', views.registration, name='registration'),
]