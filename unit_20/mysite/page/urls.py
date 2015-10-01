from django.conf.urls import include, url

from page import views

urlpatterns = [
    url(r'^(?P<pageslug>.*)/$', 'page.views.index'),
    
    url(r'^about/', views.about),
#    url(r'^news/', views.news),
    
]
