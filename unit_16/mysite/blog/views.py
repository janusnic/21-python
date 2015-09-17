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

def search_form(request):
    return render(request, 'blog/search_form.html')

def searchq(request):
    error = False
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        entries = Entry.objects.filter(headline=q)
        # entries = Entry.objects.filter(headline__contains=q)
        return render(request, 'blog/search_results.html',
            {'entries': entries, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
        # return render(request, 'blog/search_form.html', {'error': True})

def search(request):
    # error = False
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            # error = True
            errors.append('Enter a search term.')
        elif len(q) < 3:
            # error = True
            errors.append('Please enter > 3 characters.')
        else:
            # entries = Entry.objects.filter(headline=q)
            # entries = Entry.objects.filter(headline__contains=q)
            entries = Entry.objects.filter(headline__icontains=q)
            
            return render(request, 'blog/search_results.html',
                {'entries': entries, 'query': q})
    return render(request, 'blog/search_form.html',{'error': error})