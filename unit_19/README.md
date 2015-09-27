## template.Library

## inclusion_tag
```
mkdir blog/templatetags
```
categories.py

```
from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/cats.html')
def get_category_list():
    return {'cats': Category.objects.all()}

```
blog/cats.html

```
{% if cats %}
    <ul class="nav nav-sidebar">
    {% for c in cats %}
        <li>
        <a href="/blog/category/{{ c.slug }}/"> 
        {{ c.name }} 
        </a></li>
    {% endfor %}

{% else %}
    <li> <strong >There are no category present.</strong></li>

    </ul>
{% endif %}
```

## urls.py
```
    url(r'^category/(?P<categoryslug>.*)/$', 'blog.views.category'),

```

## base.html
```
{% load categories %}
{% load staticfiles %}
<!DOCTYPE html> 

{% block page %} 

<div class="container">
    <div class="row">
  
    <div class='col-sm-9'>
        {% block content %} 
        {% endblock %} 
    </div>
    <div  class='col-sm-3'>
        {% block sidebar %}
            {% block tags %}
            <div>
                {% get_category_list %}
             </div>
            {% endblock %}

            {% block recent %}
            {% endblock %}
        {% endblock %}
    </div>
</div>
</div>

{% endblock %} 


```
## views
```
def category(request, categoryslug):
    name = Category.objects.get(slug=categoryslug)
    posts = Blog.objects.filter(category=name)
    context = {'posts': posts}
    return render(request, 'blog/singlecategory.html', context)

def blog(request,blogid):
    posts_list = Entry.objects.filter(blog=blogid)
    result = {'posts_list':posts_list }

    return render(request,'blog/bloglist.html',result)


```
urls.py
```
urlpatterns = [
    url(r'^$', views.index),
    url(r'^posts/(?P<postslug>.*)/$', 'blog.views.view'),
    url(r'^blogs/(?P<blogid>.*)/$', 'blog.views.blog'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r"^add_comment/(?P<postslug>.*)/$", "blog.views.add_comment"),
    url(r'^category/(?P<categoryslug>.*)/$', 'blog.views.category'),

```
blog/singlecategory.html

```
{% extends "base.html" %}
{% block content %}
        <div id="categorieslist">
                <h2>Category {{ posts.0.category }}</h2>
                {% for post in posts %}
         <p><a href="/blog/blogs/{{ post.id }}/">{{ post.name }}</a></p>
                {% endfor %}
        </div>
{% endblock %}

```

blog/bloglist.html
```
{% extends "base.html" %} 
{% load staticfiles %}
{% block title %} {{ block.super }} - SECTION NAME {% endblock %}

{% block content %} 

<h2>Blog Index page</h2>


    {% if posts_list %}
      {% for article in posts_list %} 
        <div> 
            
            <h2><a href="/blog/posts/{{ article.slug }}/"> 
                {{ article.headline }} 
            </a></h2> 
                <span>{{ article.pub_date|date:"SHORT_DATE_FORMAT" }} | 
                      {% for author in article.authors.all %}
                      {{ author|addslashes }} 
                      {% endfor %}
                </span>
        </div> 

      {% endfor %}

    {% else %}
            <strong>There are no posts present.</strong>
    {% endif %}

{% endblock %}
```

## listlastnews listlastnews.py

```
# -*- coding: UTF-8 -*-
from django import template
from blog.models import Entry, Comment
register=template.Library()
 
@register.inclusion_tag('blog/lastnews.html') # регистрируем тег и подключаем шаблон lastnews
def lastnews():
    return {
    'last3news': Entry.objects.filter(status='1')[:3],
  }
    
```
index.html
```
{% extends "base.html" %} 
{% load staticfiles %}
{% load listlastnews %}

{% block sidebar %} 
    {{ block.super }}
    <div id="sidebar">
    {% lastnews %} 
 
    </div> 
{% endblock %}

```

# Архивы новостей

Наша задача - создать возможность группировать публикации по годам и месяцам /blog/month/{year}/{month}/

Создадим функцию month() и шаблон для просмотра архива публикаций за месяц.
Вначале создадим постраничные блоки с помощью метода  mkmonth_lst() 


```
import datetime 
import time
from calendar import month_name


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



``` 
# pytz

```
import time 
from calendar import month_name 
```

Если получили сообщение

This query requires pytz, but it isn't installed.

нужно установить pytz
```
pip install pytz
```



list.html
```
{% extends "base.html" %}
{% load listlastnews %}
{% block title %} {{ block.super }} - SECTION NAME {% endblock %}

{% block sidebar %} 
    <style type="text/css"> 
        #sidebar { float: right; border: 1px dotted #ccc; padding: 4px; } 
    </style> 
    <div id="sidebar">
    {% lastnews %} 
        Monthly Archive<br /> 
        {% for month in months %} 
            <a href="/blog/month/{{ month.0 }}/{{month.1 }}/">{{ month.2 }}</a> <br /> 
        {% endfor %} 
    </div> 
{% endblock %}

{% block content %}


<h1>Blog home page</h1>
<h2>{{ company | upper }}</h2>
<p><b>{{ author_name|capfirst }}</b></p>


     <div id="postslist">
                <!-- Posts  --> 
    <ul> 
        {% for post in posts %} 
            <div class="title">{{ post.headline }}</div> 
            <ul> 
                <div class="time">{{ post.pub_date }}</div> 
                {% autoescape off %}
                <div class="body">{{ post.body|linebreaks }}</div> 
                {% endautoescape %}
            </ul> 
        {% endfor %} 
    </ul> 

                <!-- Next/Prev page links  --> 
      {% if posts.object_list and posts.paginator.num_pages > 1 %} 
        <div class="pagination" style="margin-top: 20px; margin-left: -20px; "> 
            <span class="step-links"> 
                {% if posts.has_previous %} 
            <a href= "?page={{ posts.previous_page_number }}">newer entries &lt;&lt; </a> 
                {% endif %} 

                <span class="current"> 
                    &nbsp;Page {{ posts.number }} of {{ posts.paginator.num_pages }} 
                </span> 

                {% if posts.has_next %} 
                    <a href="?page={{ posts.next_page_number }}"> &gt;&gt; older entries</a> 
                {% endif %} 
            </span> 
        </div> 
       {% endif %}
     </div>

{% endblock %}
```

urls.py
```
from django.conf.urls import include, url

from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^posts/(?P<postslug>.*)/$', 'blog.views.view'),
    url(r'^blogs/(?P<blogid>.*)/$', 'blog.views.blog'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r"^add_comment/(?P<postslug>.*)/$", "blog.views.add_comment"),
    url(r'^category/(?P<categoryslug>.*)/$', 'blog.views.category'),
    url(r"^month/(\d+)/(\d+)/$", "blog.views.month"),
    ]

```

# views.py
```
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

```

index.html

```
{% extends "base.html" %} 
{% load staticfiles %}
{% load listlastnews %}
{% block title %} {{ block.super }} - SECTION NAME {% endblock %}

{% block sidebar %} 
    {{ block.super }}
    <div id="sidebar">
    {% lastnews %} 
    <br>
        <a href="/blog/month/{{ year }}/{{ month }}">Monthly Archive</a><br /> 
        
    </div> 
{% endblock %}

{% block content %} 
```


# django.contrib.flatpages

Добавьте django.contrib.flatpages в параметр конфигурации INSTALLED_APPS.
Пакет django.contrib.flatpages зависит от пакета django.contrib.sites, удостоверьтесь, что оба этих пакета указаны в INSTALLED_APPS.
Добавьте django.contrib.flatpages.middleware.FlatpageFallbackMiddleware в параметр конфигурации MIDDLEWARE_CLASSES.
Выполните команду manage.py migrate для установки двух необходимых таблиц в вашу базу данных.
  
```
django.contrib.flatpages
```
Добавьте параметр SITE_ID = 1 в settings.py
```
django.contrib.flatpages
```
Добавьте в urls.py
```
  urlpatterns
  = [
     url(r'^pages/',
  include('django.contrib.flatpages.urls')),
  ]
django.contrib.flatpages
```

или:

добавить 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware' в MIDDLEWARE_CLASSES setting.

Выполните manage.py migrate.


## Создать get_flatpages tag:

```
{%load flatpages%}
{%get_flatpages asflatpages %}
<ul>
   {% for page in flatpages %}
       <li><a href="{{ page.url }}">{{ page.title
}}</a></li>
   {% endfor %}
</ul>
```
##  Собственные Статические страницы
```
class Page(models.Model): 
    status = models.CharField(max_length=1, choices=BLOG_ITEM_STATUS, default='0') 
    title = models.CharField(max_length=32) 
    slug = models.SlugField(unique=True, editable=True) 
    content = models.TextField() 
    featured_image = models.ImageField(max_length=1024, 
                        null=True, blank=True, upload_to=get_blog_file_name) 

    def __str__(self): 
        return u"{}".format(self.title) 
    def __unicode__(self): 
        return self.__str__()
```
Собственные Статические страницы
```
from blog.models import Category, Post, Comment, Page

def page(request, pageslug):
    page = Page.objects.get(slug=pageslug)
    context = {'page': page, "user":request.user}
    return render_to_response('blog/page.html', context)
```
Собственные Статические страницы page.html
```
{% extends "base.html" %} 
{% load static %} 
{% block content %} 
        <div id="singlepage"> 
                <p>Title: {{ page.title }}</p> 
                <p>Body: {{ page.content }}</p> 
                {% if page.featured_image %} 
                <img src="/media/{{ page.featured_image }}"
                                 title="{{ page.title }}" /> 
                {% endif %} 
 </div> 
{% endblock %}
```
Собственные Статические страницы urls.py
```
from django.conf.urls import include, url 
from django.contrib import admin 
from django.conf import settings 
urlpatterns = [ 
   
    url(r'^blog/', include('blog.urls')), 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 
            'document_root': settings.MEDIA_ROOT, 
        }), 

    url(r'^admin/', include(admin.site.urls)), 
```
## CKEditor 
```
pip install django-ckeditor

CKEditor 
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'ckeditor',

    'blog',
)


# CKEDITOR

CKEDITOR_UPLOAD_PATH = 'plugin/ckeditor/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': '100%',
        'width': '100%',
    },
    'basic': {
        'toolbar': 'Basic',
        'height': '100%',
        'width': '100%',
    },
}
```
urls.py

```
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

]
```
models.py
```
from ckeditor.fields import RichTextField

class Page(models.Model):
    status = models.IntegerField(choices=ITEM_STATUS_CHOICES, default=ITEM_STATUS_PUBLISHED)
    title = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    #content = models.TextField()
    content = RichTextField()

    featured_image = models.ImageField(max_length=1024, 
            null=True, blank=True, upload_to=get_blog_file_name)


    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return self.__str__()
```
settings.py
```
# CKEDITOR
CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'plugin/ckeditor/')

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': '100%',
        'width': '100%',
    },
    'basic': {
        'toolbar': 'Basic',
        'height': '100%',
        'width': '100%',
    },
}

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
```

To display raw HTML  In your templates:
```
{% autoescape off %}
    {{ content }}
{% endautoescape %}
```
or:
```
{{ content|safe }}
```

To display raw HTML
```
{% extends "base.html" %}
{% block content %}
        <div id="singlepost">
                <p>{{ post.title }}</p>
                <p>
                {% autoescape off %}
                {{ post.body }}
                {% endautoescape %}
                </p>
                <p>Category: <a href="/blog/categories/{{ post.category.slug }}/">
                   {{ post.category }}</a></p>
        </div>
{% endblock %}

```
