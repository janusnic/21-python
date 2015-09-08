# 21-python

# Django Python шаблоны
# Загрузка шаблонов

Django ищет каталоги с шаблонами в соответствии с настройками загрузки шаблонов. Самый простой способ – указать каталоги с шаблонами в опции DIRS.

# Опция DIRS

По умолчанию использует значение настройки TEMPLATE_DIRS.

Настройка должна содержать список или кортеж полных путей к каталогам. 

Шаблоны могут находиться где угодно, главное, чтобы у Web-сервера были права на чтение. Расширение файла может быть любым, .html или .txt, или вообще без расширения.

Обратите внимание, пути должны быть Unix-стиле, даже для Windows.

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

Шаблон это просто текстовый файл. Он позволяет создать любой текстовый формат (HTML, XML, CSV, и др.).

Шаблон содержит переменные, которые будут заменены значениями при выполнении шаблона, и теги, которые управляют логикой шаблона.

# Переменные

Переменные выглядят таким образом: {{ variable }}. Когда шаблон встречает переменную, он вычисляет ее и заменяет результатом. Названия переменных могут состоять из букв, цифр и нижнего подчеркивания("_"). 

Используйте точку (.) для доступа к атрибутам переменной.

# когда шаблон встречает точку, он пытается получить значения в таком порядке:

- Ключ словаря

- Атрибут или метод

- Индекс списка

Если найден вызываемый объект(функция или метод), он будет вызван без аргументов. Результат будет использоваться шаблоном как значение.

Если переменная не найдена, шаблон вставит значение опции string_if_invalid, которая равна '' (пустой строке) по-умолчанию.

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
def about(request):
    mydict = {'title': 'Over and over I keep going over the world we knew','template_name':'partials/head.html'}
    return render(request,'pages/about.html', mydict)


{% include template_name %}

<h2>About Page</h2>


<h3>
{{ title }}
</h3>

<img src='/static/images/member4.jpg'>

{% include "partials/footer.html" %}

```
# Фильтры
```
# -*- coding:utf-8 -*-
from django.shortcuts import render
import datetime

class MyStruct(object): 
    pass 


def index(request):
    # return render(request,'pages/index.html', {})
    c = MyStruct()
    c.company = 'Cool Star' 
    c.title = 'Drunk, fix later' 
    c.author_name = 'Jhon Smith' 
    c.pub_date = datetime.datetime.now()
    c.exerpt  = 'I dedicate all this code, all my work, to my wife, Darlene, who will have to support me and our three children and the dog once it gets released into the public.'
    c.article_list = [{'title':'Title1','text':'text1'},{'title':'Title2','text':'text2'},{'title':'Title3','text':'text3'}]
    c.message = "When I wrote this, only God and I understood what I was doing. Now, God only knows"
    c.text = 'Вы можете изменить значение переменной используя фильтры. Фильтры выглядят таким образом: {{ name|lower }}. Это выведет значение переменной {{ name }} после применения фильтра lower к нему, который преобразует значение в нижний регистр. Используйте символ (|) для применения фильтра. I am bold font from the context Можно использовать “цепочку” фильтров. Вывод одного фильтра используется для другого. {{ text|escape|linebreaks }} обычно применяется для экранирования текста, и замены переноса строки тегами <p>.'
    return render(request, 'pages/index.html',  c.__dict__)

def about(request):
    mydict = {'title': 'Over and over I keep going over the world we knew','template_name':'partials/head.html'}
    return render(request,'pages/about.html', mydict)

```
# Вы можете изменить значение переменной используя фильтры.

- Фильтры выглядят таким образом: {{ message|lower }}. Это выведет значение переменной {{ message }} после применения фильтра lower к нему, который преобразует значение в нижний регистр. Используйте символ (|) для применения фильтра.

```
<div>

{{ message|upper }}

```

- Можно использовать “цепочку” фильтров. Вывод одного фильтра используется для другого. {{ pub_date|escape|linebreaks }} обычно применяется для экранирования текста, и замены переноса строки тегами <p>.

```
{{ pub_date|escape|linebreaks }}
```

- Некоторые фильтры принимают аргументы. Аргумент фильтра выглядит таким образом: {{ exerpt|truncatewords:30 }}. Этот код отобразит первые 130 слов переменной exerpt.

```
<p>
{{ exerpt|truncatewords:130 }}
</p>
```
- Аргументы фильтров, которые содержат пробелы, должны быть заключены в кавычки. Например, чтобы объединить список пробелом и запятой, используйте {{ exerpt|join:", " }}.

```
<div>
{{ exerpt|join:", " }}
</div>

```

Django предоставляет около шестидесяти встроенных фильтров, вот некоторые из наиболее часто используемых фильтров:

- default
Если значение равно False или пустым, будет использовано значение по умолчанию. В противном случае используется значение. Например:
```
{{ value|default:"nothing" }}
```
Если value равно "" (пустая строка), будет выведено nothing.

- length
Возвращает размер значения. Работает для строк и списков, например:

```
<div>
{{ article_list|length }}
</div>
```
- filesizeformat
Форматирует размер файла в читабельный вид (например, '13 KB', '4.1 MB', '102 bytes', и т.д.). Например:
```
{{ value|filesizeformat }}

```
Если value равно 123456789, выведет 117.7 MB.


# Теги

Теги выглядят таким образом: {% tag %}. 

Некоторые теги требуют открывающий и закрывающий теги (например, {% tag %} ... содержимое тега ... {% endtag %}).

Django содержит около двадцати встроенных тегов. 

# for
Цикл по каждому элементу массива.

```
def news(request):
    
    c = MyStruct()
    c.company = 'Cool Star' 
    c.title = 'Drunk, fix later' 
    c.pub_date = datetime.datetime.now()
    c.article_list = [{'title':'Title1','text':'text1','author_name':'Jhon Smith'},{'title':'Title2','text':'text2','author_name':'Mary Ann'},{'title':'Title3','text':'text3','author_name':'Jhon Doo'}]
        
    return render(request, 'pages/index.html',  c.__dict__)
```
# news.html
```

<h2>{{ company | upper }}</h2> 
<h2> {{ title|lower }}</h2>

{% lorem 3 p random %} 
    {% for article in article_list %} 
        <div> 
            <h2><a href="#"> 
                {{ article.title }} 
            </a></h2> 
                <span>{{ pub_date|date:"SHORT_DATE_FORMAT" }} | 
                      {{ article.author_name|addslashes }} 
                </span>
                {% lorem 1 p random %} 
        </div> 
    {% endfor %}

```

# if, elif, и else
Вычисляет переменную и если она равна “true”, выводит содержимое блока:
```
{% if article_list %}
    Number of article: {{ article_list|length }}
{% elif article_in_locker %}
    Athletes should be out soon!
{% else %}
    No article.
{% endif %}

```
если article_list не пустой, будет отображено количество article {{ article_list|length }}. Иначе, если article_in_locker не пустой, будет показано сообщение “Athletes should be out...”. Если оба списка пустые, будет показано сообщение “No article.”.

# Вы можете использовать фильтры и операторы в теге if tag:
```
{% if article_list|length > 1 %}
   Articles: {% for article in article_list %} {{ article.title }} {% endfor %} 
{% else %}
   Author: {{ article_list.0.author_name }}
{% endif %}
```
большинство шаблонных фильтров возвращает строки, таким образом, математическое сравнение результатов фильтров в общем случае будет работать не так, как вы можете ожидать. Хотя : tfilter:length является исключением.

# Комментарии

Чтобы закомментировать строку в шаблоне, используйте синтаксис комментариев: 
```
{# #}.
```

Например, этот шаблон выведет 'hello':

```
{# greeting #}hello

```

Комментарий может содержать любой код шаблона, правильный или нет. Например:

```
{# {% if foo %}bar{% else %} #}

```
Этот синтаксис может быть использован только для однострочных комментариев (нельзя использовать перенос строки между {# и #}). Если вам нужно закомментировать несколько строк, используйте тег comment.

# block и extends
Определяет наследование шаблонов 
```
{% extends "base.html" %} 


{% block content %} 

{% endblock %}

```
# Наследование шаблонов

Наследование шаблонов позволяет создать вам шаблон-“скелет”, который содержит базовые элементы вашего сайта и определяет блоки, которые могут быть переопределены дочерними шаблонами.

# base.html
```
<!DOCTYPE html> 
<html> 
    <head> 
    <title>{% block title %} SITE NAME {% endblock %}</title>
    </head> 
   <body> 
    {% block head %} 
    {% block htitle %}{% endblock %} 
    {% block menu %}{% endblock %} 
    {% endblock %} 
{% block page %} 
    {% block content %} 
    {% endblock %} 
{% endblock %} 
{% block footer %} 
    {% block copyright %} 
    {% endblock %} 
{% endblock %} 
    </body> 
</html>
```
# Дочерний шаблон:

```
{% extends "base.html" %}

{% block title %}My amazing blog{% endblock %}

{% block content %}
{% for entry in blog_entries %}
    <h2>{{ entry.title }}</h2>
    <p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}

```
- Если вы используете {% extends %}, он должен быть первым тегом в шаблоне. Иначе наследование не будет работать.

- Чем больше тегов {% block %} в вашем шаблоне, тем лучше. Помните, дочерний шаблон не обязан определять все блоки родительского, вы можете указать значение по умолчанию для всех блоков, а затем определить в дочернем шаблоне только те, которые необходимы. Лучше иметь больше “hooks”, чем меньше “hooks”.

- Если вы дублируете содержимое в нескольких шаблонах, возможно вы должны перенести его в тег {% block %} родительского шаблона.

- Если вам необходимо содержимое блока родительского шаблона, используйте переменную {{ block.super }}. Эта полезно, если вам необходимо дополнить содержимое родительского блока, а не полностью переопределить его. Содержимое {{ block.super }} не будет автоматически экранировано, так как оно уже было экранировано, при необходимости, в родительском шаблоне.

```
{% block title %} {{ block.super }} - SECTION NAME {% endblock %}
```

- Для ясности, вы можете добавить название вашему тегу {% endblock %}.
```
{% block content %}
...
{% endblock content %}
```

# Автоматическое экранирование HTML

- вы можете применять ко всем сомнительным переменным фильтр escape, который преобразует потенциально опасные HTML символы в безопасные. 

- вы можете позволить Django автоматически экранировать HTML.

# По-умолчанию в Django, каждый шаблон экранирует все переменные.
```
< заменяется на &lt;

> заменяется на &gt;

' (одинарная кавычка) заменяется на &#39;

" (двойная кавычка) заменяется на &quot;

& заменяется на &amp;
```

# Для отключения авто-экранирования для отдельных переменных, используйте фильтр safe:
```
This will be escaped: {{ data }}
This will not be escaped: {{ data|safe }}

```
# Для блоков шаблона
Для контроля авто-экранирования в шаблоне, “оберните” шаблон (или часть шаблона) тегом autoescape, например:
```
{% autoescape off %}
    Hello {{ name }}
{% endautoescape %}
```
Тег autoescape в качестве аргумента принимает on или off. В некоторых случаях, вы захотите включить экранирование в шаблоне, в котором оно было отключено. Например:
```
Auto-escaping is on by default. Hello {{ name }}

{% autoescape off %}
    This will not be auto-escaped: {{ data }}.

    Nor this: {{ other_data }}
    {% autoescape on %}
        Auto-escaping applies again: {{ name }}
    {% endautoescape %}
{% endautoescape %}
```
Тег autoescape распространяет свой эффект на шаблоны, которые наследуют текущий, и на включенные тегом include шаблоны, как и другие блочные теги. Например:

base.html
```
{% autoescape off %}
<h1>{% block title %}{% endblock %}</h1>
{% block content %}
{% endblock %}
{% endautoescape %}
```
child.html
```
{% extends "base.html" %}
{% block title %}This &amp; that{% endblock %}
{% block content %}{{ greeting }}{% endblock %}
```
Так как авто-экранирование отключено в базовом шаблоне, оно будет отключено и в дочернем шаблоне. 

# Строки и автоматическое экранирование
```
{{ data|default:"This is a string literal." }}

```
Все строки в шаблоне вставляются без автоматического экранирования – они обрабатываются как строки, к которым применили фильтр safe. Причина этого состоит в том, что автор шаблона контролирует содержимое этих строк и самостоятельно может убедиться при создании шаблона, что они не содержат не безопасных символов.

Это означает, чтобы вы должны писать:
```
{{ data|default:"3 &lt; 2" }}
```
...вместо:
```
{{ data|default:"3 < 2" }}  {# Bad! Don't do this. #}
```
Это правило не распространяется на переменные, которые используются в качестве аргументов, так как автор шаблоне не может контролировать содержимое этих переменных.

# Вызов методов

Вызов большинства методов объектов также доступен в шаблоне. Это означает, что шаблон имеет доступ не только к атрибутам классов (например, название поля) и переменных переданных из представлениях. 

```
{% for comment in task.comment_set.all %}
    {{ comment }}
{% endfor %}

```
Также, QuerySets предоставляет метод count() для получения количества объектов. Следовательно, вы можете получить количество комментариев связанных с конкретной задачей:
```
{{ task.comment_set.all.count }}
```
# base2.html
```
{% extends "base.html" %} 
{% block page %} 
    {% block content %} 
    {% endblock %} 

    {% block sidebar %} 
    {% endblock %} 
{% endblock %}

```

# home/base.html

```
{% extends "base2.html" %} 
{% block title %} 
    Блог 
{% endblock %} 
{% block sidebar %} 
    {% block tags %} 
    {% endblock %} 

    {% block recent %} 
    {% endblock %} 
{% endblock %}

```

# news.html

```
{% extends "home/base.html" %} 

{% block title %} {{ block.super }} - SECTION NAME {% endblock %}
{% block content %}
<h2>{{ company | upper }}</h2> 
<h2> {{ title|lower }}</h2>

{% lorem 3 p random %} 
    {% for article in article_list %} 
        <div> 
            <h2><a href="#"> 
                {{ article.title }} 
            </a></h2> 
                <span>{{ pub_date|date:"SHORT_DATE_FORMAT" }} | 
                      {{ article.author_name|addslashes }} 
                </span>
                {% lorem 1 p random %} 
        </div> 
    {% endfor %}

{% endblock %}

```