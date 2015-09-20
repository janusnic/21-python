## Модель User имеет такие поля

- username;
- password;
- email address;
- first name;
- surname.
- is_active 

```
./manage.py startapp myauth

```
## models.py:
```
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
```
ImageField имеет upload_to атрибут. Его значение ссылается на MEDIA_ROOT установку. Если MEDIA_ROOT проекта - /prj/media/  тогда upload_to attribute = profile_images - /prj/media/profile_images/.

Django ImageField поле использует Python Imaging Library (PIL). http://pillow.readthedocs.org/en/latest/installation.html

## Application definition
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
)

```
admin.py 
```
from myauth.models import UserProfile

admin.site.register(UserProfile)

$ python manage.py makemigrations myauth
$ python manage.py migrate
```

## Создаем UserForm и UserProfileForm

myauth/forms.py
```
from django import forms
from django.contrib.auth.models import User
from myauth.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

```
## Создаем register() View

views.py:
```
from django.shortcuts import render

from myauth.forms import UserForm, UserProfileForm

def register(request):

    # boolean value
    # Установлено в False при инициализации. Изменим на True при успешной регистрации.
    registered = False

    # Если HTTP POST, обработаем форму.
    if request.method == 'POST':
        # Получаем информацию из форм.
        # Мы используем две формы UserForm и UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Если обе формы прошли проверку...
        if user_form.is_valid() and profile_form.is_valid():
            # Сохраним данные пользователя из формы в database.
            user = user_form.save()

       # Хешируем пароль с помощью set_password method.

            user.set_password(user.password)
            user.save()

            # Пока пользователь настраивает свой профиль не выполнять commit=False.

            profile = profile_form.save(commit=False)
            profile.user = user

            # Юзер хочет картинку?
            # Если да, предоставим ему поле для ввода картинки.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Сохранить экземпляр модели UserProfile.
            profile.save()

            # Изменить переменную при успешной регистрации.
            registered = True

        # Ошибки?
        # Печать ошибок на terminal.
        else:
            print user_form.errors, profile_form.errors

    # Не HTTP POST, строим два эеземпляра ModelForm .
    # Эти формы пустые , предназначены для пользовательских вводов.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'myauth/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


```
## Создаем шаблон Registration

myauth/register.html:

```
<!DOCTYPE html>
<html>
    <head>
        <title>Janus Blog</title>
    </head>

    <body>
        <h1>Register with Janus</h1>

        {% if registered %}
        Janus says: <strong>thank you for registering!</strong>
        <a href="/blog/">Return to the homepage.</a><br />
        {% else %}
        Janus says: <strong>register here!</strong><br />

        <form id="user_form" method="post" action="/myauth/register/"
                enctype="multipart/form-data">

            {% csrf_token %}

            <!-- Display each form. The as_p method wraps each element in a paragraph
                 (<p>) element. This ensures each element appears on a new line,
                 making everything look neater. -->
            {{ user_form.as_p }}
            {{ profile_form.as_p }}

            <!-- Provide a button to click to submit the form. -->
          <input type="submit" name="submit" value="Register" />
        </form>
        {% endif %}
    </body>
</html>
```

## Путь для register()

myauth/urls.py:
```
from django.conf.urls import include, url

from myauth import views

urlpatterns = [
    
    url(r'^register/$', 'myauth.views.register', name='register'),
 
]
```
urls.py:
```

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('page.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^blog/', include('blog.urls')),

    url(r'^myauth/', include('myauth.urls')),
    url(r'^$',TemplateView.as_view(template_name='index.html')),
    url(r'^contact/thankyou/', 'contact.views.thankyou'),
    url(r'^contact/', 'contact.views.contactview'),

    url(r'^contactus/', contview.contact),
    url(r'^test2/([0-9]{4})/([0-9]{2})/', urlviews.test2),

]

```

index.html template
```
<a href="/myauth/register/">Register Here</a>
```
## Создаем login() View

myauth/views.py:
```
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
def user_login(request):

    # If the request is a HTTP POST
    if request.method == 'POST':

       # Эта информация получена из login form.
       # Мы используем request.POST.get('<variable>') вместо  request.POST['<variable>'],
       # потому что request.POST.get('<variable>') вернет None, если значение не существует,
       # в то время ка request.POST['<variable>'] вернет key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверка username/password
        user = authenticate(username=username, password=password)

        # Если создан объект user
        # с необходимыми правами -  credentials
        if user:
            # Если account active? Он может быть disabled.
            if user.is_active:
            # Если account правильный и активный, можно логиниться.
                # Переадресуем пользователя на страницу blog.
                login(request, user)
                return HttpResponseRedirect('/blog/')
            else:
                # Используется неактивный account - no logging in!
                return HttpResponse("Your Blog account is disabled.")
        else:
       # Bad login 
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    # Запрос не HTTP POST, поэтому показываем login form.
    else:
        # Не переданы variables в template system
        # пустой dictionary object...
        return render(request, 'myauth/login.html', {})
```
## Создаем Login Template templates/myauth/login.html :

```
<!DOCTYPE html>
<html>
    <head>
        <!-- Is anyone getting tired of repeatedly entering the header over and over?? -->
        <title>Blog</title>
    </head>

    <body>
        <h1>Login to Blog</h1>

        <form id="login_form" method="post" action="/myauth/login/">
            {% csrf_token %}
            Username: <input type="text" name="username" value="" size="50" />
            <br />
            Password: <input type="password" name="password" value="" size="50" />
            <br />

            <input type="submit" value="submit" />
        </form>

    </body>
</html>
```
## Путь для Login View to a URL

urls.py:
```
from django.conf.urls import include, url

from myauth import views

urlpatterns = [
    
    url(r'^register/$', 'myauth.views.register', name='register'),
    url(r'^login/$', 'myauth.views.user_login', name='login'),
 ]
```
## blog/index.html

<a href="/myauth/login/">Login</a>

```
<h2>Blog Index page</h2>
        <a href="/myauth/login/">Login</a>

        {% if user.is_authenticated %}
        <h1>Blog says... hello {{ user.username }}!</h1>
        {% else %}
        <h1>Blog says... hello world!</h1>
        {% endif %}
```

## Restricting Access
```
def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")
```

## Restricting Access с помощью Decorator

views.py:
```
from django.contrib.auth.decorators import login_required

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

```
urls.py
```
from django.conf.urls import include, url

from myauth import views

urlpatterns = [
    
    url(r'^register/$', 'myauth.views.register', name='register'),
    url(r'^login/$', 'myauth.views.user_login', name='login'),
    url(r'^restricted/', 'myauth.views.restricted', name='restricted'),
    

]
```
settings.py:
```
LOGIN_URL = '/myauth/login/'
```
## Logging Out

user_logout():
```
from django.contrib.auth import logout

# Use the login_required() decorator to ensure only those logged in can access the view.

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/blog/')
```
## URL /myauth/logout/
urls.py:
```
from django.conf.urls import include, url

from myauth import views

urlpatterns = [
    
    url(r'^register/$', 'myauth.views.register', name='register'),
    url(r'^login/$', 'myauth.views.user_login', name='login'),
    url(r'^restricted/', 'myauth.views.restricted', name='restricted'),
    url(r'^logout/$', 'myauth.views.user_logout', name='logout'),

]
```
## Django template code.
base.html:
```
{% load staticfiles %}
<!DOCTYPE html> 
<html lang="ru">
    <head>
        <meta charset="utf-8" />
       <title>{% block title %} SITE NAME {% endblock %}</title>
        <link href="{% static "css/bootstrap.css" %}" rel="stylesheet">
        <style>
            body {
                padding-top: 60px; /* 60px to make the container 
                                go all the way to the bottom of the topbar */
            }
        </style>
        <link href="{% static "css/navbar-fixed-top.css" %}" rel="stylesheet">
        <!--[if lt IE 9]>
        <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
<boby>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">Janus Tiny Blog</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="/">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="/blog">Blog</a></li>
            


          <ul class="nav navbar-nav navbar-right">
                         
                {% if user.is_authenticated %}
                <li><a href="/blog">hello {{ user.username }}!</a></li>
                <li><a href="/myauth/logout/">Logout</a></li>
                {% else %}
                <li><a href="/myauth/login/">Login</a></li>
                <li><a href="/myauth/register/">Register Here</a></li>
                {% endif %}
            
            <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    {% block head %} 
    {% block htitle %}{% endblock %} 
    {% block menu %}{% endblock %} 
    {% endblock %} 
{% block page %} 
<div class="container">
    {% block content %} 
    {% endblock %} 
</div>
{% endblock %} 
{% block footer %} 
    {% block copyright %} 
    {% endblock %} 
{% endblock %} 
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>

<script src="{% static "js/bootstrap.js" %}" type="text/javascript"></script>
        {% block extrahead %}
        {% endblock %}

    </body> 
</html>


```

# декоратор
## Функции в Python'e являются объектами

Для того, чтобы понять, как работают декораторы, в первую очередь следует осознать, что в Python'е функции — это тоже объекты.
```
def shout(word="да"): 
    return word.capitalize()+"!" 
 print shout() # выведет: 'Да!' 
``` 
Так как функция - это объект - связать её с переменнной, как и любой другой объект 
```
scream = shout 
```
Заметьте, что мы не используем скобок: мы НЕ вызываем функцию "shout", мы связываем её с переменной "scream". Это означает, что теперь мы можем вызывать "shout" через "scream": 
```
print scream() # выведет: 'Да!' 
```
Более того, это значит, что мы можем удалить "shout", и функция всё ещё будет доступна через переменную "scream" 
```
del shout 
try: 
    print shout() 
except NameError, e: 
    print e     #выведет: "name 'shout' is not defined" 
 
print scream() # выведет: 'Да!'
```
функция в Python'e может быть определена… внутри другой функции!
```
def talk(): 
    # Внутри определения функции "talk" мы можем определить другую... 
    def whisper(word="да"): 
        return word.lower()+"..."; 
    # ... и сразу же её использовать! 
    print whisper() 
```
Теперь, КАЖДЫЙ РАЗ при вызове "talk", внутри неё определяется а затем и вызывается функция "whisper". 
```
talk() # выведет: "да..." 
```
Но вне функции "talk" НЕ существует никакой функции "whisper": 
```
try: 
    print whisper() 
except NameError, e: 
    print e 
    #выведет : "name 'whisper' is not defined"
```
## Ссылки на функции
Теперь мы знаем, что функции являются полноправными объектами, а значит:
- могут быть связаны с переменной;
- могут быть определены одна внутри другой.

это значит, что одна функция может вернуть другую функцию!
```
def getTalk(type="shout"): 
    # Мы определяем функции прямо здесь 
    def shout(word="да"): 
        return word.capitalize()+"!" 
 
    def whisper(word="да") : 
        return word.lower()+"..."; 

    # Затем возвращаем необходимую 
    if type == "shout": 
# мы НЕ используем "()", нам нужно не вызвать функцию, 
        # а вернуть объект функции 
        return shout 
    else: 
        return whisper 
``` 

Возьмём функцию и свяжем её с переменной 
```
talk = getTalk() 
```
Как мы можем видеть, "talk" теперь - объект "function": 
```
print talk 
```
> выведет: <function shout at 0xb7ea817c> 
Который можно вызывать, как и функцию, определённую "обычным образом": 
```
print talk() 
```
Если нам захочется - можно вызвать её напрямую из возвращаемого значения: 
```
print getTalk("whisper")() # выведет: да...
```
мы можем и передавать её другой функции, как параметр:
```
def doSomethingBefore(func): 
    print "Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал" 
    print func() 
 doSomethingBefore(scream) 
```

декораторы — это, по сути, просто своеобразные «обёртки», которые дают нам возможность делать что-либо до и после того, что сделает декорируемая функция, не изменяя её.

## Создадим свой декоратор «вручную»
# Декоратор - это функция, ожидающая ДРУГУЮ функцию в качестве параметра 
```
def my_shiny_new_decorator(a_function_to_decorate): 
    # Внутри себя декоратор определяет функцию-"обёртку". 
    # Она будет (что бы вы думали?..) обёрнута вокруг декорируемой, 
    # получая возможность исполнять произвольный код до и после неё. 

    def the_wrapper_around_the_original_function(): 
        # Поместим здесь код, который мы хотим запускать ДО вызова 
        # оригинальной функции 
        print "Я - код, который отработает до вызова функции" 
 
        # ВЫЗОВЕМ саму декорируемую функцию 
        a_function_to_decorate() 

        # А здесь поместим код, который мы хотим запускать ПОСЛЕ вызова оригинальной функции 
        print "А я - код, срабатывающий после" 
    # На данный момент функция "a_function_to_decorate" НЕ ВЫЗЫВАЛАСЬ НИ РАЗУ 
   # Теперь, вернём функцию-обёртку, которая содержит в себе 
    # декорируемую функцию, и код, который необходимо выполнить до и после. 
    # Всё просто! 
    return the_wrapper_around_the_original_function 
```
Представим теперь, что у нас есть функция, которую мы не планируем больше трогать. 
```
def a_stand_alone_function(): 
    print "Я простая одинокая функция, ты ведь не посмеешь меня изменять?.." 
 
a_stand_alone_function() 
# выведет: Я простая одинокая функция, ты ведь не посмеешь меня изменять?.. 
# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть 
# Просто передать декоратору, который обернет исходную функцию в любой код, 
# который нам потребуется, и вернёт новую, готовую к использованию функцию: 
 
a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function) 
a_stand_alone_function_decorated() 
#выведет: 
# Я - код, который отработает до вызова функции 
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?.. 
# А я - код, срабатывающий после
```
теперь мы бы хотели, чтобы каждый раз, во время вызова a_stand_alone_function, вместо неё вызывалась a_stand_alone_function_decorated. 

перезапишем a_stand_alone_function функцией, которую нам вернул my_shiny_new_decorator:
```
a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
#выведет:
# Я - код, который отработает до вызова функции
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
# А я - код, срабатывающий после
```
Вот так можно было записать предыдущий пример, используя синтаксис декораторов:
```
@my_shiny_new_decorator 
def another_stand_alone_function(): 
    print "Оставь меня в покое" 
 
another_stand_alone_function() 
#выведет: 
# Я - код, который отработает до вызова функции 
# Оставь меня в покое 
# А я - код, срабатывающий после
```
@decorator — просто синтаксический сахар для конструкций вида:
```
another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)
```
Декораторы — это просто pythonic-реализация паттерна проектирования «Декоратор». В Python включены некоторые классические паттерны проектирования, такие как рассматриваемые в этой статье декораторы, или привычные любому пайтонисту итераторы.
```
def makebold(fn): 
    def wrapped(): 
        return "<b>" + fn() + "</b>" 
    return wrapped 
 
def makeitalic(fn): 
    def wrapped(): 
        return "<i>" + fn() + "</i>" 
    return wrapped 
 
@makebold 
@makeitalic 
def hello(): 
    return "hello habr" 
 
print hello() ## выведет <b><i>hello habr</i></b>
```
можно вкладывать декораторы друг в друга, например так:
```
def bread(func): 
    def wrapper(): 
        print "</------\>" 
        func() 
        print "<\______/>" 
    return wrapper 
 
def ingredients(func): 
    def wrapper(): 
        print "#помидоры#" 
        func() 
        print "~салат~" 
    return wrapper 
 
def sandwich(food="--ветчина--"): 
    print food 
 
sandwich() 
#выведет: --ветчина-- 
sandwich = bread(ingredients(sandwich)) 
sandwich() 
#выведет: 
# </------\> 
# #помидоры# 
# --ветчина-- 
# ~салат~ 
# <\______/>
И используя синтаксис декораторов:

@bread 
@ingredients 
def sandwich(food="--ветчина--"): 
    print food 
 
sandwich() 
#выведет: 
# </------\> 
# #помидоры# 
# --ветчина-- 
# ~салат~ 
# <\______/> 
```
Следует помнить о том, что порядок декорирования ВАЖЕН:
```
@ingredients 
@bread 
def sandwich(food="--ветчина--"): 
    print food 
 
sandwich() 
#выведет: 
# #помидоры# 
# </------\> 
# --ветчина-- 
# <\______/> 
# ~салат~
```