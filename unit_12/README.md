# 21-python

# Django Python URLS

# Как Django обрабатывает запрос

- Django определяет какой корневой модуль URLconf использовать. Обычно, это значение настройки ROOT_URLCONF, но, если объект запроса HttpRequest содержит атрибут urlconf, его значение будет использоваться вместо ROOT_URLCONF.

- Django загружает модуль конфигурации URL и ищет переменную urlpatterns. Это должен быть список экземпляров django.conf.urls.url().

- Django перебирает каждый URL-шаблон по порядку, и останавливается при первом совпадении с запрошенным URL-ом.

- Если одно из регулярных выражений соответствует URL-у, Django импортирует и вызывает соответствующее представление, которое является просто функцией Python (или представление-класс). 

```

# ROOT_URLCONF = 'mysite.urls'

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

```

# При вызове передаются следующие аргументы:

# Объект HttpRequest.

- Если в результате применения регулярного выражения получили именованные совпадения, они будут переданы как позиционные аргументы.

- Именованные аргументы создаются из именованных совпадений. Они могут быть перезаписаны значениями из аргумента kwargs, переданного в django.conf.urls.url().

- Если ни одно регулярное выражение не соответствует, или возникла ошибка на любом из этапов, Django вызывает соответствующий обработчик ошибок. 

Например

```
from django.conf.urls import include, url
from django.contrib import admin
from testurl import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test1/', views.test1),
   
]

```

Не нужно добавлять косую черту в начале, потому что каждый URL содержит ее. 

Символ 'r' перед каждым регулярным выражением не обязателен, но рекомендуется. Он указывает Python что строка “сырая(raw)” и ничего в строке не должно быть экранировано. 

# views.py

```
from django.http import HttpResponse
# Create your views here.

def test1(request):
    return HttpResponse('Hello from Test1 Page')

```

# request.GET

```

def index(request):
    if 'q' in request.GET:
        message = 'You submitted: %r' % request.GET['q']
    else:
        message = 'You submitted nothing!'

    return HttpResponse('Hello from Home Page'+message)

```

# Python regexes

```
import re

r = re.compile(r'^test2/([0-9]{4})/([0-9]{2})/')

if r.match('test2/1234/88/'):
...     print "all done"
... 
all done

```

# Для получения совпадающего значения из URL, просто добавьте скобки 

```
http://127.0.0.1:8000/test2/2015/09/

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test1/', views.test1),
    
    url(r'^test2/([0-9]{4})/', views.test2),

    url(r'^test2/([0-9]{4})/([0-9]{2})/', views.test3),

    url(r'^test2/([0-9]{4})/([0-9]{2})/([0-9]+)/', views.test4),
    
]

```
# # views.py

```

def test1(request):
    return HttpResponse('Hello from Test1 Page')


def test3(request, year, month):
    return HttpResponse('Hello from Test2 '+ str(year) +' - ' + str(month) + ' Page')

```


# Именованные группы

вы можете использовать имена для групп и значения будут передаваться как именованные аргументы.

Для регулярных выражений в Python синтаксис для именованных совпадений выглядит таким образом 

```
(?P<name>pattern)

```
где name это название группы, а pattern – шаблон.


# пример конфигурации URL, переписанный с использованием именованных групп:

```

r = re.compile(r'^blog/(?P<num>\d+)/$')

r.match('blog/1234').groups()

('1234',)


url(r'^blog/(?P<num>\d+)', views.page),

```

# HttpResponse objects¶
# views.py

```
def page(request, num='1'):

    def page(request, num='1'):

    response = HttpResponse("Here's the text of the Web page it's ", content_type="text/plain")
  
    
    if num == '90':
        response = str(response)+'Cool!'
   
    return HttpResponse(str(response))
```

```
def page(request, num='1'):

    response = HttpResponse("Here's the text of the Web page it's ")
 
    
    if num == '90':
        response = str(response)+'Cool!'
    elif num == '99':
        response = HttpResponse()
        response.write("<p>Here's the text of the Web page.</p>")
        response.write("<p>Here's another paragraph.</p>")

   
    return HttpResponse(str(response))
```

# Производительность

Каждое регулярное выражение в urlpatterns будет скомпилировано при первом использовании. Это делает систему невероятно быстрой.

# Синтаксис переменной urlpatterns

urlpatterns должен быть списком экземпляров url().

# Обработчики ошибок

Если Django не может найти подходящий шаблон URL, или было вызвано исключение в процессе обработки запроса, Django вызовет соответствующее представление обрабатывающее ошибку.

# Эти представления определены в четырёх переменных. 

- handler404
- handler500
- handler403
- handler400


# page_not_found() переопределяется handler404:
- handler404 = 'mysite.views.my_custom_page_not_found_view'
# server_error() переопределяется handler500:
- handler500 = 'mysite.views.my_custom_error_view'
# permission_denied() переопределяется handler403:
- handler403 = 'mysite.views.my_custom_permission_denied_view'
# bad_request() переопределяется handler400:
- handler400 = 'mysite.views.my_custom_bad_request_view'

# TemplateView
```
from django.views.generic import TemplateView

url(r'^$',TemplateView.as_view(template_name='index.html')),

```

TemplateDoesNotExist at /
index.html

# settings.py
```
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

# Настройка статики

- Убедитесь что django.contrib.staticfiles добавлено INSTALLED_APPS.

- В настройках укажите STATIC_URL, например:
```
STATIC_URL = '/static/'



STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
 
)

```

В шаблоне или “захардкодьте” URL /static/images/gallery-image-3.jpg, или лучше использовать тег static для генерация URL-а по указанному относительному пути с использованием бэкенда, указанного в STATICFILES_STORAGE (это позволяет легко перенести статические файлы на CDN).
```
{% load staticfiles %}
<img src="{% static "images/gallery-image-3.jpg" %}" alt="My image"/>

```

- Сохраните статические файлы в каталоге static вашего приложения. Например static/images/gallery-image-3.jpg.

# Раздача файлов
Кроме конфигурации, необходимо настроить раздачу статических файлов.

При разработке, если вы используете django.contrib.staticfiles, это все происходит автоматически через runserver, при DEBUG равной True.

Настройка STATICFILES_DIRS указывает каталоги, которые проверяются на наличие статических файлов. По умолчанию эта настройка пустая. Например:

```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
)
```


# django.contrib.staticfiles. 
Он собирает статичные файлы из каждого вашего приложения (и из других мест, которые вы укажете) в единое место, которое может легко применяться на боевом сервере.

- Разместите следующий код в файле стилей (polls/static/polls/style.css):

```
/static/css/styles.css

h2 {
    color: green;
}

```
- Затем добавьте следующие строки в начало /templates/index.html:

```
{% load staticfiles %}

<link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}" />

```
Тэг {% load staticfiles %} загружает шаблонный тег {% static %} из шаблонной библиотеки staticfiles. Шаблонные тег {% static %} создаёт абсолютный URL на статичный файл.


- Добавление фонового изображения

Затем добавьте следующие строки в файл стилей (polls/static/polls/style.css):

```
/static/css/styles.css
body {
    background: gray url(../images/background.png);
}
```



# Landing Page
```
url(r'^$',TemplateView.as_view(template_name='land/index.html')),

```


# Комбинирование URLconfs
```
./manage.py createapp page 
```
В любой момент, ваш urlpatterns может “включать” другие модули URLconf.

```

from django.conf.urls import include, url

urlpatterns = [
    # ... snip ...
    url(r'^pages/', include('page.urls')),
    url(r'^contact/', include('contact.urls')),
    # ... snip ...
]

```

Заметим, что регулярные выражения не содержат $ (определитель конца строки), но содержит косую черту в конце. Каждый раз, когда Django встречает include() (django.conf.urls.include()), из URL обрезается уже совпавшая часть, остальное передается во включенный URLconf для дальнейшей обработки.

# page/urls.py

```
from django.conf.urls import include, url
from page import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^about/', views.about),
]

```
# page/views.py
```

from django.shortcuts import render

# Create your views here.

def index(request):
    pass

def about(request):
    pass
```

# render

```
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'pages/index.html', {})

def about(request):
    return render(request,'pages/about.html', {})

```

# {}

```

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'pages/index.html', {})

def about(request):
    mydict = {'title': 'Over and over I keep going over the world we knew'}
    return render(request,'pages/about.html', mydict)

```

# templates/pages/about.html

```
<h2>About Page</h2>

<h3>
{{ title }}

</h3>

```


# include
Загружает шаблон и выводит его с текущим контекстом. Это способ “включить” один шаблон в другой.

Названия шаблона можно указать переменной или строкой в одинарных или двойных кавычках.

```
<h2>About Page</h2>


<h3>
{{ title }}
</h3>

<img src='/static/images/member4.jpg'>

{% include "partials/footer.html" %}

```
Этот пример включает содержимое шаблона, чье имя содержится в переменной template_name:

```
{% include template_name %}

```