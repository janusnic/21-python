from django.shortcuts import render
from .models import Entry
# Create your views here.

def index(request):
    result = Entry.objects.all()
    return render(request,'blog/index.html',{'result':result})
