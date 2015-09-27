from django.shortcuts import render, render_to_response
from .models import Entry, Category, Comment, Blog

from blog.forms import CommentForm

from django.http import HttpResponseRedirect

from django.core.paginator import Paginator, InvalidPage, EmptyPage

import datetime 
import time
from calendar import month_name
# Create your views here.

def index(request):
    # result = Entry.objects.all()
    posts_list = Entry.objects.order_by('-pub_date')
    year, month = time.localtime()[:2]
    
    paginator = Paginator(posts_list, 2)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts_list = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts_list = paginator.page(paginator.num_pages)
    
    category_list = Category.objects.order_by('name')
        
    result = {'categories_list':category_list, 'posts_list':posts_list,'year':year, 'month': month }

    return render(request,'blog/index.html',result)

def blog(request,blogid):
    posts_list = Entry.objects.filter(blog=blogid)
    result = {'posts_list':posts_list }

    return render(request,'blog/bloglist.html',result)



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


def mkmonth_lst():
    """Make a list of months to show archive links."""

    if not Entry.objects.count(): return []

    # set up vars
    year, month = time.localtime()[:2]
    first = Entry.objects.order_by("pub_date")[0]
    fyear = first.pub_date.year
    fmonth = first.pub_date.month
    months = []

    # loop over years and months
    for y in range(year, fyear-1, -1):
        start, end = 12, 0
        if y == year: start = month
        if y == fyear: end = fmonth-1

        for m in range(start, end, -1):
            months.append((y, m, month_name[m]))
    return months

def month(request, year, month):
    """Monthly archive."""

    posts = Entry.objects.filter(pub_date__year=year, pub_date__month=month)

    paginator = Paginator(posts, 2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("blog/list.html", dict(posts=posts, user=request.user, months=mkmonth_lst(),  archive=True))


def category(request, categoryslug):
    name = Category.objects.get(slug=categoryslug)
    posts = Blog.objects.filter(category=name)
    context = {'posts': posts}
    return render(request, 'blog/singlecategory.html', context)
