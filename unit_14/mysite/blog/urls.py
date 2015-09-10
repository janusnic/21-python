from django.conf.urls import include, url

from blog import views

urlpatterns = [
    url(r'^$', views.index),
    ]
