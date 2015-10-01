## использование модуля uuid

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

manage.py startapp page

```
PAGE_STATUS_PUBLISHED = 1
PAGE_STATUS_HIDDEN = 2
PAGE_STATUS_CHOICES = (
    (PAGE_STATUS_PUBLISHED, "Published"),
    (PAGE_STATUS_HIDDEN, "Hidden"),
)

class Page(models.Model):
    status = models.IntegerField(choices=PAGE_STATUS_CHOICES, default=PAGE_STATUS_PUBLISHED)
    title = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    # content = RichTextField()
    #widgets = models.ManyToManyField(Widget, null=True, blank=True)
    featured_image = models.ImageField(max_length=1024, null=True, blank=True, upload_to=get_page_file_name)
    related_slider = models.ForeignKey(Slider, null=True, blank=True)

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return self.__str__()

```
# Application definition
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'myauth',
    'page',
)

```
## helper

models.py
```
from utils import helpers

def get_page_file_name(instance, filename):
    return helpers.get_file_filename(instance, filename, "static/images/page")

```

## Способы генерации уникальных ID

использование модуля uuid из стандартной библиотеки python. 
Модуль предоставляет возможность генерации уникальных ID 
четырьмя методами, которые описаны в RFC4122

для случая, если нужно сгенерировать случайный ID, используется uuid4
uuid.uuid4()

## utils/helpers.py
```
import datetime
import uuid
import os


def get_file_filename(instance, filename, folder):
    current_date = datetime.date.today()
    path = u"{}/{}/{}/".format(folder, current_date.year, current_date.month)  # It is real path address

    file_uuid = str(uuid.uuid4())
    file_name, file_extension = os.path.splitext(filename)
    name = u"{}{}".format(file_uuid, file_extension)

    full_filename = unicode(os.path.join(path, name).lower())

    return full_filename

```

## Собственные Статические страницы


page/views.py

```
from django.shortcuts import render
from page.models import Page

def index(request, pageslug):
    page = Page.objects.get(slug=pageslug)
    context = {'page': page}
    return render(request,'pages/index.html', context)

```
urls.py
```
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('page.urls')),
    url(r'^home/', include('home.urls')),
```

page/urls.py
```
from django.conf.urls import include, url

urlpatterns = [
    url(r'^(?P<pageslug>.*)/$', 'page.views.index'),
]

```
page/index.html

```
{% extends "base.html" %}
{% load staticfiles %}

{% block content %}
    <div class="row">
        <div class="col-md-12">
            {% if page.featured_image %}

                <img src="/{{ page.featured_image }}" title="{{ page.title }}" />
            {% endif %}
            <h1>{{ page.title }}</h1>
            <p>
                {{ page.content|safe }}
            </p>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            {% if page.related_slider %}
                {% include "blog/_slider.html" with slider=page.related_slider %}
            {% endif %}
        </div>
    </div>
{% endblock %}

```

## Slider models.py

```
from django.db import models
from utils import helpers

PAGE_STATUS_PUBLISHED = 1
PAGE_STATUS_HIDDEN = 2
PAGE_STATUS_CHOICES = (
    (PAGE_STATUS_PUBLISHED, "Published"),
    (PAGE_STATUS_HIDDEN, "Hidden"),
)

def get_page_file_name(instance, filename):
    return helpers.get_file_filename(instance, filename, "static/images/page")


class Slider(models.Model):
    status = models.IntegerField(choices=PAGE_STATUS_CHOICES, default=PAGE_STATUS_PUBLISHED)
    title = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return self.__str__()


class Slide(models.Model):
    status = models.IntegerField(choices=PAGE_STATUS_CHOICES, default=PAGE_STATUS_PUBLISHED)
    title = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(max_length=1024, null=True, blank=True, upload_to=get_page_file_name)
    related_slider = models.ForeignKey(Slider)

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return self.__str__()

class Page(models.Model):
    status = models.IntegerField(choices=PAGE_STATUS_CHOICES, default=PAGE_STATUS_PUBLISHED)
    title = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    
    featured_image = models.ImageField(max_length=1024, null=True, blank=True, upload_to=get_page_file_name)
    related_slider = models.ForeignKey(Slider, null=True, blank=True)

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return self.__str__()

```


## Slider admin.py

```
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from page.models import Slide, Slider, Page
from redactor.widgets import RedactorEditor

# Register your models here.
class SlideInline(admin.TabularInline):
    model = Slide
    extra = 1

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    inlines = [SlideInline, ]

# Page
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
        fields = '__all__'

admin.site.register(Page, PageAdmin)
admin.site.register(Slider, SliderAdmin)

```
## Slider pages.html

```
{% extends "base.html" %}
{% load static %}

{% block content %}
    <div class="row">
        <div class="col-md-12">
            {% if page.featured_image %}
                <img src="{{ page.featured_image }}" title="{{ page.title }}" />
            {% endif %}
            <h1>{{ page.title }}</h1>
            <p>
                {{ page.content|safe }}
            </p>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            {% if page.related_slider %}
                {% include "blog/_slider.html" with slider=page.related_slider %}
            {% endif %}
        </div>
    </div>
{% endblock %}

```

## Slider _slider.html

```

<div id="application-bootstrap-carousel" class="carousel slide" data-ride="carousel">
    {# Indicators #}
    <ol class="carousel-indicators">
        {% for slide in slider.slide_set.all %}
            <li data-target="#slide-{{ forloop.counter0 }}" data-slide-to="{{ forloop.counter0 }}"
                    {% if forloop.counter0 == 0 %} class="active" {% endif %}></li>
        {% endfor %}
    </ol>

    {# Wrapper for slides #}
    <div class="carousel-inner">
        {% for slide in slider.slide_set.all %}
            <div {% if forloop.counter0 == 0 %} class="item active" {% else %} class="item" {% endif %}>
                <img src="/{{ slide.image }}"
                     alt="{{ slide.title }}" title="{{ slide.title }}" />
                <div class="carousel-caption">
                    <h3>{{ slide.title }}</h3>
                    <p>{{ slide.description }}</p>
                </div>
            </div>
        {% endfor %}
    </div>

    {# Controlls #}
    <a class="left carousel-control" href="#application-bootstrap-carousel" role="button" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left"></span>
    </a>
    <a class="right carousel-control" href="#application-bootstrap-carousel" role="button" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right"></span>
    </a>
</div>
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

Считаем посетителей
```
from django.shortcuts import render, render_to_response, redirect

def track_url(request):
    post_id = None
    url = '/blog/'
    if request.method == 'GET':
        if 'post_id' in request.GET:
            post_id = request.GET['post_id']
            try:
                post = Entry.objects.get(id=post_id)
                post.rating = post.rating + 1
                post.save()
                url = post.url
            except:
                pass

    return redirect(url)

```
Считаем посетителей
```
urlpatterns = [
   
    url(r'^goto/$', 'blog.views.track_url', name='goto'),

]
```
Считаем посетителей
```
{% block content %}
        <div id="singlepost">
                
                
                <li>
                <a href="{% url 'goto' %}?post_id={{result.id}}">{{ result.headline }}</a>
                {% if result.rating > 1 %}
                    ({{ result.rating }} views)
                {% elif result.rating == 1 %}
                    ({{ result.rating }} view)
                {% endif %}
                </li>
                
```
index.html
```
{% if posts_list %}
      {% for article in posts_list %} 
        <div> 
            
            <h2><a href="/blog/posts/{{ article.slug }}/"> 
                {{ article.headline }} 
            </a></h2> 
                <span>{{ article.pub_date|date:"SHORT_DATE_FORMAT" }} | 
                      {% for author in article.authors.all %}
                      {{ author|addslashes }} 
                      {% endfor %} | 
                      {% if article.rating > 1 %}
                        ({{ article.rating }} views)
                        {% elif article.rating == 1 %}
                        ({{ article.rating }} view)
                        {% endif %}
                </span>
        </div> 


      {% endfor %}
```

views.py
```


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

        
    try:
        post = Entry.objects.get(slug=postslug)
        post.rating = post.rating + 1
        post.save()
        
    except:
        pass

    

    context = {'result': result, "comments":comments,"form":CommentForm(), "user":request.user}
    return render(request,'blog/view.html', context)

```
Set up Heroku
```
https://dashboard.heroku.com/
https://toolbelt.heroku.com/
```
Set up Heroku
```
$ heroku login
```
Set up Heroku
```
$ pip install django-toolbelt
```
Procfile
```
# web: gunicorn myapp.wsgi

web: gunicorn myapp.wsgi --log-file -

# web: waitress-serve --port=$PORT janusdg.wsgi:application
```
Dependencies
```
$ pip freeze > requirements.txt
```
Dependencies
```
boto==2.38.0
cryptacular==1.4.1
dj-database-url==0.3.0
dj-static==0.0.6
Django==1.8.3
django-flatpages-tinymce==0.1.1
django-herokuapp==0.9.20
django-require==1.0.8
django-require-s3==1.0.0
django-storages==1.1.8
django-wysiwyg-redactor==0.4.7
Markdown==2.6.2
pbkdf2==1.3
Pillow==2.8.1
psycopg2==2.6.1
pytz==2015.4
selenium==2.46.0
sh==1.11
waitress==0.8.9
gunicorn==19.1.1
static==0.4
wsgiref==0.1.2
```
wsgi.py
```
import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
```

settings.py
```
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from django.utils.crypto import get_random_string

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
```
settings.py
```
# A secret key used for cryptographic algorithms.

SECRET_KEY = os.environ.get("SECRET_KEY", get_random_string(50, 
     "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []

HEROKU_APP_NAME = "janusdg"

SITE_NAME = "Janus Django Site"

SITE_DOMAIN = "janusdg.herokuapp.com"

PREPEND_WWW = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ALLOWED_HOSTS = (
    SITE_DOMAIN,
    "{HEROKU_APP_NAME}.herokuapp.com".format(
        HEROKU_APP_NAME = HEROKU_APP_NAME,
    ),
)
```
settings.py
```
ROOT_URLCONF = 'janusdg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
settings.py
```
WSGI_APPLICATION = 'janusdg.wsgi.application'

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(default='postgres://localhost'),
}
```
settings.py
```
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, "static"),
)

# Namespace for cache keys, if using a process-shared cache.

CACHE_MIDDLEWARE_KEY_PREFIX = "janusdg"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    # Long cache timeout for staticfiles, since this is used heavily by the optimizing storage.
    "staticfiles": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 60 * 60 * 24 * 365,
        "LOCATION": "staticfiles",
    },
}
```
settings.py
```
# Logging configuration.

LOGGING = {
    "version": 1,
    # Don't throw away default loggers.
    "disable_existing_loggers": False,
    "handlers": {
        # Redefine console logger to run in production.
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        # Redefine django logger to use redefined console logging.
        "django": {
            "handlers": ["console"],
        }
    }
}
```
settings.py
```
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from django.utils.crypto import get_random_string

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
```
Deploy
```
$ touch .gitignore

Open it and write:

myenv

*.pyc
```
$ git init

$ git add .

$ git commit -m “First commit of my django app”

$ heroku create appnameonheroku

$ git push heroku master

$ heroku open

$ heroku ps:scale web=1
```
PostgreSQL
```
heroku addons
=== Resources for janusdg
Plan                         Name                   Price
---------------------------  ---------------------  -----
heroku-postgresql:hobby-dev  building-sweetly-8133  free

=== Attachments for janusdg
Name      Add-on                 Billing App
--------  ---------------------  -----------
DATABASE  building-sweetly-8133  janusdg
```
PostgreSQL
```
heroku pg:info
=== DATABASE_URL
Plan:        Hobby-dev
Status:      Available
Connections: 0/20
PG Version:  9.4.4
Created:     2015-08-11 10:33 UTC
Data Size:   6.4 MB
Tables:      0
Rows:        0/10000 (In compliance)
Fork/Follow: Unsupported
Rollback:    Unsupported
Add-on:      building-sweetly-8133
```
PostgreSQL
```
heroku run python manage.py syncdb

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

    
## Redactor WYSIWYG editor
Pillow or PIL # for image upload
```
pip install django-wysiwyg-redactor

Redactor WYSIWYG editor
INSTALLED_APPS = (
    # ...
    'redactor',
    # ...
)

REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'
```
Redactor WYSIWYG editor
```
from redactor.widgets import RedactorEditor

class PostAdminForm(forms.ModelForm):
    class Meta:
    model = Post
    fields = '__all__'
    widgets = {
           'body': RedactorEditor(),
        }

class PostAdmin(admin.ModelAdmin):
  form = PostAdminForm
  prepopulated_fields = {'slug': ('title',)}
  list_display = ('title', 'category', 'author', 'status')
  search_fields = ['title']

Redactor WYSIWYG editor
short_text = RedactorField(
    verbose_name=u'Text',
    redactor_options={'lang': 'en', 'focus': 'true'},
    upload_to='tmp/',
    allow_file_upload=True,
    allow_image_upload=True
)
```
 Redactor WYSIWYG editor
```
INSTALLED_APPS = (
    # ...
    'redactor',
    # ...
)
```
Add url(r'^redactor/', include('redactor.urls')), to urls.py
```
urlpatterns = [
    # ...
    url(r'^redactor/', include('redactor.urls')),
    # ...
]

```

Add default config in settings.py
```
REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'

```
