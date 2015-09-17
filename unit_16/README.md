# Формы в Django

## Search blog/search_form.html
```
<html>
<head>
    <title>Search</title>
</head>
<body>
    {% if error %}
        <p style="color: red;">Please submit a search term.</p>
    {% endif %}
    <form action="/blog/search/" method="get">
        <input type="text" name="q">
        <input type="submit" value="Search">
    </form>
</body>
</html>
```

## views.py
```

def searchq(request):
    error = False
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        entries = Entry.objects.filter(headline=q)
        return render(request, 'blog/search_results.html',
            {'entries': entries, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

```
## blog/search_results.html
```
<p>You searched for: <strong>{{ query }}</strong></p>

{% if entries %}
    <p>Found {{ entries|length }} entry{{ entries|pluralize }}.</p>
    <ul>
        {% for entry in entries %}
        <li>{{ entry.headline }}</li>
        {% endfor %}
    </ul>
{% else %}
    <p>No entries matched your search criteria.</p>
{% endif %}
```
## urls.py
```
from django.conf.urls import include, url

from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^posts/(?P<postslug>.*)/$', 'blog.views.view'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    ]

```

## views.py
```
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) < 3:
            error = True
        else:
            
            # entries = Entry.objects.filter(headline__contains=q)
            entries = Entry.objects.filter(headline__icontains=q)
            
            return render(request, 'blog/search_results.html',
                {'entries': entries, 'query': q})
    return render(request, 'blog/search_form.html',{'error': error})
```
## Search blog/search_form.html
```
<html>
<head>
    <title>Search</title>
</head>
<body>
    {% if error %}
        <p style="color: red;">Please submit a search term. Term must be > 3 char</p>
    {% endif %}
    <form action="/blog/search/" method="get">
        <input type="text" name="q">
        <input type="submit" value="Search">
    </form>
</body>
</html>
```
## views.py
```
def search(request):
    
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            
            errors.append('Enter a search term.')
        elif len(q) < 3:
            
            errors.append('Please enter > 3 characters.')
        else:
            
            entries = Entry.objects.filter(headline__icontains=q)
            
            return render(request, 'blog/search_results.html',
                {'entries': entries, 'query': q})
    return render(request, 'blog/search_form.html',{'error': error})
```

## Search blog/search_form.html

```
<html>
<head>
    <title>Search</title>
</head>
<body>
    {{% if errors %}
        <ul>
            {% for error in errors %}
            <li>{{ error }}</li>
            {% endfor %}
        </ul>
    {% endif %}
    <form action="/blog/search/" method="get">
        <input type="text" name="q">
        <input type="submit" value="Search">
    </form>
</body>
</html>
```
```
 ./manage.py startapp contactform
```
### urls.py
```
from django.conf.urls import patterns, include, url
from django.contrib import admin
from contactform import views as contview
from testurl import views as urlviews
from django.views.generic import TemplateView

urlpatterns = [

    url(r'^contactus/', contview.contact),

```

### views.py
```
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('Enter your name.')
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
          try:
            send_mail(
                request.POST['name'],
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'support@ruunalbe.com'),
                ['siteowner@example.com'],
            )
            return HttpResponse('Thank you, form has been submitted successfully')
          except Exception, err: 
            return HttpResponse(str(err))
    return render(request, 'contactform/contact_form.html',{'errors': errors})
```

## Формы и CSRF защита

Django поставляется с защитой против Cross Site Request Forgeries. При отправке формы через POST с включенной защитой от CSRF вы должны использовать шаблонный тег csrf_token.


##@ contactform/contact_form.html

```
<!doctype html>
<html>
<head>
    <title>Contact us</title>
</head>
<body>
    <h1>Contact us</h1>

    {% if errors %}
        <ul>
            {% for error in errors %}
            <li>{{ error }}</li>
            {% endfor %}
        </ul>
    {% endif %}

    <form action="/contactus/" method="post">
        {% csrf_token %}
        <p>Name: <input type="text" name="name"></p>
        <p>Subject: <input type="text" name="subject"></p>
        <p>Your e-mail (optional): <input type="text" name="email"></p>
        <p>Message: <textarea name="message" rows="10" cols="50"></textarea></p>
        <input type="submit" value="Submit">
    </form>
</body>
</html>

```
## form redisplay
# views.py
```
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'contact_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
    })
```
# contact_form.html
```
<html>
<head>
    <title>Contact us</title>
</head>
<body>
    <h1>Contact us</h1>

    {% if errors %}
        <ul>
            {% for error in errors %}
            <li>{{ error }}</li>
            {% endfor %}
        </ul>
    {% endif %}

    <form action="/contact/" method="post">
        <p>Subject: <input type="text" name="subject" value="{{ subject }}"></p>
        <p>Your e-mail (optional): <input type="text" name="email" value="{{ email }}"></p>
        <p>Message: <textarea name="message" rows="10" cols="50">**{{ message }}**</textarea></p>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```


## Класс Django Form
Как и модель в Django, которая описывает структуру объекта, его поведение и представление, Form описывает форму, как она работает и показывается пользователю.

Поля формы сами являются классами. Они управляют данными формы и выполняют их проверку при отправке формы. Например, DateField и FileField работают с разными данными и выполняют разные действия с ними.

Поле формы представлено в браузере HTML “виджетом” - компонент интерфейса. 

Каждый тип поля представлен по умолчанию определенным классом Widget, который можно переопределить при необходимости.

## Создание, обработка и рендеринг форм

При рендеринге объекта в Django мы обычно:

- получаем его в представлении (например, загружаем из базы данных)

- передаем в контекст шаблона

- представляем в виде HTML в шаблоне, используя переменные контекста

Рендеринг форм происходит аналогичным образом с некоторыми отличиями.

Экземпляр модели, который используется в представлении, обычно загружается из базы данных. При работе с формой мы обычно создаем экземпляр формы в представлении.

При создании формы мы может оставить её пустой, или добавить начальные данные

## Создание формы

Рассмотрим форму, которая может быть использована для реализации функционала “свяжитесь с нами” на личном веб сайте:

При отправке формы будет отправлен POST запрос с данными из формы.

Также необходимо добавить представление, которое обрабатывает запрос на URL.


## Создание форм в Django
### Класс Form

```
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
```
В этом случае, форма содержит поля: name, subject, message, email и cc_myself. CharField, EmailField и BooleanField – это просто три стандартных типа поля; 

Экземпляр Form содержит метод is_valid(), который выполняет проверку всех полей формы. Если все данные правильные, это метод:

- вернет True

- добавит данные формы в атрибут cleaned_data.

### Представление

Данные формы отправляются обратно в Django и обрабатываются представлением, обычно тем же, которое и создает форму. Это позволяет повторно использовать часть кода.

Для обработки данных формой нам необходимо создать ее в представлении для URL, на который браузер отправляет данные формы:

```
from django.shortcuts import render
from django.http import HttpResponseRedirect

def contactview(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/contact/thankyou/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

     return render(request, 'contact/contacts.html', {'form': form})
```
Если в представление пришел GET запрос, будет создана пустая форма и добавлена в контекст шаблона для последующего рендеринга. Это мы и ожидаем получить первый раз открыв страницу с формой.

Если форма отправлена через POST запрос, представление создаст форму с данными из запроса: form = NameForm(request.POST) Это называется “привязать данные к форме” (теперь это связанная с данными форма).

Мы вызываем метод is_valid() формы. Если получили не True, снова рендерим шаблон, передав нашу форму. Теперь форма не пустая (не связана с данными) и HTML форма будет содержать ранее отправленные данные, их можно повторно отредактировать и отправить снова.

Если is_valid() вернет True, мы можем найти проверенные данные в атрибуте cleaned_data. Мы можем сохранить эти данные в базе данных, или выполнить какие-то другие действия над ними, перед тем, как сделать редирект на другую страницу.

### Шаблон

Наш contacts.html шаблон может быть довольно простым:
```
<form action="" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit" />
</form>
```
Все поля формы и их атрибуты будут добавлены в HTML из {{ form }} при рендеринге шаблона.


## Модели и формы

Если ваша форма будет использоваться для создания или редактирования объекта модели, вы можете использовать ModelForm. Она поможет сэкономить много времени и кода, т.к. позволяет создать форму по классу модели.

## Связанные и не связанные с данными экземпляры формы

Незаполненная форма не содержит данных, привязанных к её полям. При отображении формы пользователь увидит её пустой или содержащей значения по умолчанию.

Заполненная форма содержит переданную информацию и, следовательно, может быть использована для проверки введённых данных. При отображении заполненной формы, не прошедшей проверку, она будет содержать встроенные сообщения об ошибках, которые расскажут пользователю о причинах отказа в принятии его данных.

Атрибут формы is_bound позволяет узнать связана форма с данными или нет.

## Поля формы

### Виджеты
Каждое поле формы содержит соответствующий класс Widget, который отвечает за создание HTML кода, представляющего поле, например input type="text".

В большинстве случаев поле уже содержит подходящий виджет. Например, по умолчанию поле CharField представлено виджетом TextInput, который создает тег input type="text" в HTML. Если вам вместо него необходим textarea, вы можете указать подходящий виджет при определении поля формы.

```
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

```
### Данные поля
Когда в форму добавлены данные, и она проверена методом is_valid() (и is_valid() вернул True), проверенные данные будут добавлены в словарь form.cleaned_data. Эти данные будет преобразованы в подходящий тип Python.

В приведённом ранее примере, cc_myself будет булевым значением. Аналогично, такие поля как IntegerField и FloatField преобразовывают свои значения в типы Python int и float соответственно.

```
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
```

как можно обрабатывать данные в представлении, к которому привязана форма:
```
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django import forms
from contact.forms import ContactForm

from django.core.mail import send_mail, BadHeaderError

def contactview(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(email)
            send_mail(name, subject, message, email, recipients)
            return HttpResponseRedirect('/contact/thankyou/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact/contacts.html', {'form': form})

def thankyou(request):
        return render_to_response('contact/thankyou.html')
```

### form.cleaned_data
```
# views.py

from django.shortcuts import render
from mysite.contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
```


Некоторые поля требуют дополнительной обработки. Например, загруженные файлы необходимо обрабатывать по другому (их можно получить из request.FILES, а не request.POST). 
```
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact/contact_form.html', {'form': form})
```
## Работа с шаблонами формы

Чтобы получить доступ к форме в шаблоне, просто передайте экземпляр в контекст шаблона. Если ваша форма добавлена в контекст как form, {{ form }} создаст необходимые теги label и input.

## HTML5 поля и проверка в браузере

Если ваша форма содержит URLField, EmailField или одно из числовых полей, Django будет использовать url, email и number поля ввода HTML5. По умолчанию браузеры могут выполнять собственную проверку для этих полей, некоторые проверки могут быть более строгие чем в Django. Если вы хотите отключить это, добавьте novalidate атрибут в тег form, или используйте другой виджет для этих полей, например TextInput.

Все формы являются дочерними классами django.forms.Form, включая ModelForm, которые вы можете увидеть в админке Django.

## Настройки рендеринга формы

форма не добавляет тег form и submit кнопку. Вы должны добавить их самостоятельно.
Вы можете использовать следующие варианты рендеринга label/input:

- {{ form.as_table }} выведет их в таблице, в ячейках тега tr

- {{ form.as_p }} обернет их в тег p

- {{ form.as_ul }} выведет в теге li

тег table или ul вы должны добавить сами.

Вот результат {{ form.as_p }} для нашей формы ContactForm:
```
<p><label for="id_subject">Subject:</label>
    <input id="id_subject" type="text" name="subject" maxlength="100" /></p>
<p><label for="id_message">Message:</label>
    <input type="text" name="message" id="id_message" /></p>
<p><label for="id_sender">Sender:</label>
    <input type="email" name="sender" id="id_sender" /></p>
<p><label for="id_cc_myself">Cc myself:</label>
    <input type="checkbox" name="cc_myself" id="id_cc_myself" /></p>

```
Следует отметить, что каждое поле формы обладает атрибутом с идентификатором id_field-name, с помощью которого обеспечивается связь с тегом метки. Это позволяет формам быть дружественными к вспомогательным технологиям. Также вы можете настроить способ генерации меток и идентификаторов.

### {{ form.as_table }}
```
# contact_form.html

<html>
<head>
    <title>Contact us</title>
</head>
<body>
    <h1>Contact us</h1>

    {% if form.errors %}
        <p style="color: red;">
            Please correct the error{{ form.errors|pluralize }} below.
        </p>
    {% endif %}

    <form action="" method="post">
        <table>
            {{ form.as_table }}
        </table>
        {% csrf_token %}
        <input type="submit" value="Submit">
    </form>
</body>
</html>

```
## Рендеринг полей вручную
Мы можем не использовать полный рендеринг формы и отрендерить каждое поле отдельно (например, чтобы поменять порядок полей). Каждое поле формы можно получить через атрибут формы {{ form.name_of_field }}. Например:
```
{{ form.non_field_errors }}
<div class="fieldWrapper">
    {{ form.subject.errors }}
    <label for="{{ form.subject.id_for_label }}">Email subject:</label>
    {{ form.subject }}
</div>
<div class="fieldWrapper">
    {{ form.message.errors }}
    <label for="{{ form.message.id_for_label }}">Your message:</label>
    {{ form.message }}
</div>
<div class="fieldWrapper">
    {{ form.sender.errors }}
    <label for="{{ form.sender.id_for_label }}">Your email address:</label>
    {{ form.sender }}
</div>
<div class="fieldWrapper">
    {{ form.cc_myself.errors }}
    <label for="{{ form.cc_myself.id_for_label }}">CC yourself?</label>
    {{ form.cc_myself }}
</div>
```
Элемент label также может быть создан с помощью метода label_tag(). 
```
<div class="fieldWrapper">
    {{ form.subject.errors }}
    {{ form.subject.label_tag }}
    {{ form.subject }}
</div>
```
## Рендеринг ошибок проверки
За гибкость мы платим количеством кода. До этого мы не заботились о выводе ошибок проверки, т.к. Django делал это за нас. В этом примере нам пришлось явно выводить ошибки проверки для каждого поля и для всей формы. Обратите внимание на {{ form.non_field_errors }} в начале в формы и вывод ошибок для каждого поля.

Список ошибок можно вывести используя {{ form.name_of_field.errors }}. Они будут выглядеть приблизительно как:
```
<ul class="errorlist">
    <li>Sender is required.</li>
</ul>
```
Списку назначен CSS-класс errorlist, что позволяет вам настроить параметры его отображения. Если потребуется более тонкая настройка отображения ошибок, вы можете это организовать с помощью цикла по ним:
```
{% if form.subject.errors %}
    <ol>
    {% for error in form.subject.errors %}
        <li><strong>{{ error|escape }}</strong></li>
    {% endfor %}
    </ol>
{% endif %}
```
Ошибки, не относящиеся к полям, (и/или ошибки скрытых полей, которые отображаются наверху формы при использовании методов подобных form.as_p()) будут отображаться с дополнительным классом nonfield, что поможет их отделить от ошибок полей формы. Например, {{ form.non_field_errors }} может выглядеть так:
```
<ul class="errorlist nonfield">
    <li>Generic validation error</li>
</ul>
```
## Цикл по полям формы

Если вы используете однотипный HTML для каждого поля формы, вы можете избежать дублирования кода, используя тег {% for %} для прохода по полям формы:
```
{% for field in form %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
    </div>
{% endfor %}



    {% if form.errors %}
        <p style="color: red;">
            Please correct the error{{ form.errors|pluralize }} below.
        </p>
    {% endif %}

    
    <div class="field{% if form.message.errors %} errors{% endif %}">
        {% if form.message.errors %}
            <ul>
            {% for error in form.message.errors %}
                <li><strong>{{ error }}</strong></li>
            {% endfor %}
            </ul>
        {% endif %}
        <label for="id_message">Message:</label>
        {{ form.message }}
    </div>
```
### Полезные атрибуты {{ field }}:

- {{ field.label }}
Метка поля, т.е. Email address.

- {{ field.label_tag }}
Метка поля, обёрнутая в соответствующий HTML тег label. Также включает атрибут формы label_suffix. Например, по умолчания label_suffix содержит двоеточие:
```
<label for="id_email">Email address:</label>
{{ field.id_for_label }}

```
ID, которое будет использоваться для этого поля (id_email). Вы можете использовать его вместо label_tag, если самостоятельно генерируете label для поля. Так полезно при генерации JavaScript, если вы не хотите “хардкодить” ID.

- {{ field.value }}
Значение поля, например someone@example.com.

- {{ field.html_name }}
Имя поля, которое будет использовано в HTML-поле. Здесь учитывается префикс формы, если он был установлен.

- {{ field.help_text }}
Любой вспомогательный текст, который привязан к полю.

- {{ field.errors }}
Вывод <ul class="errorlist">, содержащий все ошибки валидации, относящиеся к полю. Вы можете настраивать представление списка ошибок с помощью цикла {% for error in field.errors %}. В этом случае, каждый объект в цикле является простой строкой, содержащей сообщение об ошибке.

- {{ field.is_hidden }}
Значение этого атрибута равно True, если поле является скрытым, и False в противном случае. Данный атрибут обычно не используется при выводе формы, но может быть полезен в условиях подобных этому:
```
{% if field.is_hidden %}
   {# Do something special #}
{% endif %}
{{ field.field }}
```
Экземпляр Field из класса формы, который обёрнут с помощью BoundField. Он предоставляет доступ к атрибутам Field, например {{ char_field.field.max_length }}.

### Цикл по скрытым и отображаемым полям
Если вы вручную размещаете форму в шаблоне, то у вас появляется возможность трактовать поля вида input type="hidden" по своему. Например, так как скрытые поля не отображаются на форме, размещение сообщений об ошибке для поля “перейти далее” может смутить пользователей. Такие ошибки следует обрабатывать другим способом.

Django предоставляет два метода, которые позволяют организовать раздельные циклы по скрытым и отображаемым полям: hidden_fields() и visible_fields(). Покажем как изменится наш пример, если воспользоваться этими методами:
```
{# Include the hidden fields #}
{% for hidden in form.hidden_fields %}
{{ hidden }}
{% endfor %}
{# Include the visible fields #}
{% for field in form.visible_fields %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
    </div>
{% endfor %}
```

Этот пример не обрабатывает ошибки в скрытых полях. Обычно ошибка в скрытом поле означает наличие подмены в форме, так как обычный сценарий работы с формами не предполагает изменения этих полей. Тем не менее, вы можете реализовать отображение таких ошибок формы.

### Повторное использование шаблонов форм
Если на вашем сайте используется однотипная логика отображения форм, вы можете избежать дублирования кода, сохранив цикл по полям формы в отдельном шаблоне и подключая его в другие шаблоны с помощью тега include:
```
# In your form template:
{% include "form_snippet.html" %}

# In form_snippet.html:
{% for field in form %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
    </div>
{% endfor %}
```
Если объект формы, переданный в шаблон, имеет другое имя в контексте, вы можете создать для него псевдоним, используя аргумент with тега include:
```
{% include "form_snippet.html" with form=comment_form %}
```
Если вам придётся делать такое часто, то можно создать собственный включающий тег.


## Validation Rules
```
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

```

### Specifying labels
```
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)
```

