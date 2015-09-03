from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'pages/index.html', {})

def about(request):
    mydict = {'title': 'Over and over I keep going over the world we knew'}
    return render(request,'pages/about.html', mydict)