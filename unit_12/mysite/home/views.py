from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    if 'q' in request.GET:
        message = 'You submitted: %r' % request.GET['q']
    else:
        message = 'You submitted nothing!'

    return HttpResponse('Hello from Home Page'+message)

def page(request, num='1'):

    response = HttpResponse("Here's the text of the Web page it's ")
 
    
    if num == '90':
        response = str(response)+'Cool!'
    elif num == '99':
        response = HttpResponse()
        response.write("<p>Here's the text of the Web page.</p>")
        response.write("<p>Here's another paragraph.</p>")

   
    return HttpResponse(str(response))