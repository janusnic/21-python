from django.shortcuts import render, render_to_response
from .models import Entry, Category, Comment

from blog.forms import CommentForm

from django.http import HttpResponseRedirect

from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.

def index(request):
    # result = Entry.objects.all()
    posts_list = Entry.objects.order_by('-pub_date')
    paginator = Paginator(posts_list, 2)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts_list = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts_list = paginator.page(paginator.num_pages)
    
    category_list = Category.objects.order_by('name')
        
    result = {'categories_list':category_list, 'posts_list':posts_list }

    return render(request,'blog/index.html',result)

    
def view(request, postslug):
    result = Entry.objects.get(slug=postslug)

    comments = Comment.objects.filter(post=result)

    paginator = Paginator(comments, 2)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        comments = paginator.page(page)
    except (InvalidPage, EmptyPage):
        comments = paginator.page(paginator.num_pages)

        

    context = {'result': result, "comments":comments,"form":CommentForm(), "user":request.user}
    return render(request,'blog/view.html', context)


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

def add_comment(request, postslug):
    """Add a new comment."""
    p = request.POST
    if p["body"]:
        author = request.user
        comment = Comment(post=Entry.objects.get(slug=postslug))
        cf = CommentForm(p, instance=comment)

        cf.fields["author"].required = False
        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect('/blog/')

