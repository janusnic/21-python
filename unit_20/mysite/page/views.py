# -*- coding:utf-8 -*-
from django.shortcuts import render
from page.models import Page
import datetime


def index(request, pageslug):
    page = Page.objects.get(slug=pageslug)
    context = {'page': page}
    return render(request,'pages/index.html', context)


def about(request):
    mydict = {'title': 'Over and over I keep going over the world we knew','template_name':'partials/head.html'}
    return render(request,'pages/about.html', mydict)
