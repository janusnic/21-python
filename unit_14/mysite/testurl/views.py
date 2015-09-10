from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test1(request):
    return HttpResponse('Hello from Test1 Page')


def test2(request, year, month):
    return HttpResponse('Hello from Test2 '+ str(year) +' - ' + str(month) + ' Page')



def index(request):
    if 'q' in request.GET:
        message = 'You submitted: %r' % request.GET['q']
    else:
        message = 'You submitted nothing!'

    return HttpResponse('Hello from Home Page'+message)

