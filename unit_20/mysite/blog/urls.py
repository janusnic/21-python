from django.conf.urls import include, url

from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^posts/(?P<postslug>.*)/$', 'blog.views.view'),
    url(r'^blogs/(?P<blogid>.*)/$', 'blog.views.blog'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r"^add_comment/(?P<postslug>.*)/$", "blog.views.add_comment"),
    url(r'^category/(?P<categoryslug>.*)/$', 'blog.views.category'),
    url(r"^month/(\d+)/(\d+)/$", "blog.views.month"),
    url(r'^goto/$', 'blog.views.track_url', name='goto'),
    ]
