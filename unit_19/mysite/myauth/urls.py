from django.conf.urls import include, url

from myauth import views

urlpatterns = [
    
    url(r'^register/$', 'myauth.views.register', name='register'),
    url(r'^login/$', 'myauth.views.user_login', name='login'),
    url(r'^restricted/', 'myauth.views.restricted', name='restricted'),
    url(r'^logout/$', 'myauth.views.user_logout', name='logout'),

]