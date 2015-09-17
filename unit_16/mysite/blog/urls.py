from django.conf.urls import include, url

from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^posts/(?P<postslug>.*)/$', 'blog.views.view'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    ]
