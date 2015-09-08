"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
# from home import views
from testurl import views as urlviews
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('page.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^$',TemplateView.as_view(template_name='index.html')),
    #url(r'^$',TemplateView.as_view(template_name='land/index.html')),
    url(r'^test1/', urlviews.test1),
    url(r'^test2/([0-9]{4})/([0-9]{2})/', urlviews.test2),
    # url(r'^test/', views.index, name='home'),
    # url(r'^blog/$', views.page),
    # url(r'^blog/(?P<num>\d+)', views.page),
]
