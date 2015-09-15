from django.shortcuts import render, render_to_response
from .models import Entry, Category
# Create your views here.

def index(request):
    # result = Entry.objects.all()
    posts_list = Entry.objects.order_by('headline')
    
    category_list = Category.objects.order_by('name')
        
    result = {'categories_list':category_list, 'posts_list':posts_list }

    return render(request,'blog/index.html',result)


def view(request, postslug):
    result = Entry.objects.get(slug=postslug)

    context = {'result': result}
    return render_to_response('blog/view.html', context)
