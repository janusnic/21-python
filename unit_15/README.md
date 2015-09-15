# Интерфейс администратора Django

Интерфейс администратора по умолчанию включен, если вы создавали проект командой startproject.

Интерфейс администратора имеет четыре зависимости 
- django.contrib.auth, 
- django.contrib.contenttypes, 
- django.contrib.messages 
- django.contrib.sessions. 

Если эти приложения не входят в список INSTALLED_APPS, добавьте их.

## Интерфейс администратора

Определите, какие модели будут редактироваться через интерфейс администратора.

Для каждой модели вы можете создать класс ModelAdmin, который инкапсулирует настройки интерфейса администратора для конкретной модели.

### models.py
```

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):              # __str__ on Python 3
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):              # __str__ on Python 3
        return u'%s %s' % (self.first_name, self.last_name)

```

### ./manage.py makemigrations blog

You are trying to add a non-nullable field 'first_name' to author without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now()
>>> ''

###  ./manage.py migrate

## Объект ModelAdmin

### class ModelAdmin
Класс ModelAdmin – это отображение модели в интерфейсе администратора. Его код добавляют обычно в файл admin.py вашего приложения. 

## Настройки ModelAdmin

### Настройки ModelAdmin
- ModelAdmin.actions_on_top
- ModelAdmin.actions_on_bottom

Определяет где на странице будет расположены панели с действиями. По умолчанию эта панель расположена сверху (actions_on_top = True; actions_on_bottom = False).

### ModelAdmin.actions_selection_counter
Указывает отображать ли счетчик выбранных объектов после списка действий. По умолчанию он отображается (actions_selection_counter = True).

### ModelAdmin.exclude
Этот атрибут должен содержать список полей, которые не будут включены в форму редактирования.


## author list_display admin.py

```
from django.contrib import admin

# Register your models here.
from .models import Category, Blog, Author, Entry 

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


admin.site.register(Author, AuthorAdmin)

admin.site.register(Category)

admin.site.register(Blog)

admin.site.register(Entry)
```

### search_fields AuthorAdmin:

```
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


admin.site.register(Author, AuthorAdmin)
```
### EntryAdmin list_filter = ('pub_date',)

```
class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)


admin.site.register(Author, AuthorAdmin)

admin.site.register(Category)

admin.site.register(Blog)

admin.site.register(Entry, EntryAdmin)
```

## ModelAdmin.date_hierarchy
Укажите в date_hierarchy название DateField или DateTimeField поля вашей модели, и страница списка объектов будет содержать навигацию по датам из этого поля.

### date_hierarchy = 'pub_date'
```

class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'

```
### ordering = ('-pub_date',)
```

class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
```


## ModelAdmin.fields
Если вам необходимо внести небольшие изменения форму на странице редактирования и добавления, например, изменить список отображаемых полей, их порядок или сгруппировать их, вы можете использовать настройку fields

### fields
```
class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('blog', 'headline', 'authors', 'body_text', 'pub_date', 'n_comments', 'n_pingbacks', 'rating' )


```
Чтобы поля отображались в одной строке, укажите их в кортеже вместе. В этом примере, поля headline и slug будут отображаться в одном ряду:

```
class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('blog', ('headline', 'slug') 'authors', 'body_text', 'pub_date', 'n_comments', 'n_pingbacks', 'rating' )

```

### filter_horizontal = ('authors',)
```
class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('blog', 'headline', 'authors', 'body_text', 'pub_date', 'n_comments', 'n_pingbacks', 'rating' )
    filter_horizontal = ('authors',)

```
### Select blog raw_id_fields

```
class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('blog', 'headline', 'authors', 'body_text', 'pub_date', 'n_comments', 'n_pingbacks', 'rating' )
    filter_horizontal = ('authors',)
    raw_id_fields = ('blog',)


```

## SlugField в Django

### class SlugField([max_length=50, **options])

Slug – газетный термин. “Slug” – это короткое название-метка, которое содержит только буквы, числа, подчеркивание или дефис. В основном используются в URL.

Как и для CharField, можно указать max_length. Если max_length не указан, Django будет использовать значение 50.

Устанавливает Field.db_index в True, если аргумент явно не указан.

Обычно значение SlugField создается на основе какого-то другого значения(например, название статьи). Это может работать автоматически в интерфейсе администрации благодаря параметру prepopulated_fields.

```

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug   = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):              # __str__ on Python 3
        return self.name
    
class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __unicode__(self):              # __str__ on Python 3
        return self.headline

    class Meta: 
        ordering = ['pub_date'] 

```

$ python manage.py makemigrations blog 

```
sqlite> delete from blog_category;
sqlite> vacuum;
sqlite> delete from blog_entry;
sqlite> vacuum;
sqlite> .exit
```

$ python manage.py migrate 

### SlugField
Обычно значение SlugField создается на основе какого-то другого значения(например, название статьи). Это может работать автоматически в интерфейсе администрации благодаря параметру prepopulated_fields.

### ModelAdmin.prepopulated_fields
prepopulated_fields позволяет определить поля, которые получают значение основываясь на значениях других полей:
```
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
```
Указанные поля будут использовать код JavaScript для заполнения поля значением на основе значений полей-источников. Основное применение - это генерировать значение для полей SlugField из значений другого поля или полей. Процесс генерирования состоит в объединении значений полей-источников и преобразованию результата в правильный “slug” (например, заменой пробелов на дефисы).

prepopulated_fields не принимает поля DateTimeField, ForeignKey или ManyToManyField.

```
from django.contrib import admin

# Register your models here.
from .models import Category, Blog, Author, Entry 

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('blog', 'headline', 'slug', 'authors', 'body_text', 'pub_date', 'n_comments', 'n_pingbacks', 'rating' )
    filter_horizontal = ('authors',)
    raw_id_fields = ('blog',)
    prepopulated_fields = {"slug": ("headline",)}


admin.site.register(Author, AuthorAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Blog)

admin.site.register(Entry, EntryAdmin)
```

## Действия администратора

административный интерфейс Django позволяет создать и зарегистрировать “действия” – простые функции, которые вызываются для выполнения неких действий над списком объектов, выделенных на странице интерфейса.
 
Django поставляется с действием “удалить выделенные объекты”, которое доступно для всех моделей.
 
## Создание действий
Стандартной задачей, которую мы возможно будем выполнять с моделью Entry, будет изменение состояний статьи с “черновик” на “опубликовано”. Мы легко сможем выполнить это действие в интерфейсе администратора для одной статьи за раз, но если потребуется выполнить массовую публикацию группы статей, то вы столкнётесь с нудной работой. Таким образом, следует написать действие, которое позволит нам изменять состояние статьи на “опубликовано.”
 

### Добавим поле выбора в модель
```
BLOG_ENTRY_STATUS = (
    ('0', 'Dratf'),
    ('1', 'Published'),
    ('2', 'Not Published'),
)

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    slug   = models.SlugField(unique=True)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    status = models.CharField(max_length=1, choices=BLOG_ENTRY_STATUS, default='0')

    def __unicode__(self):              # __str__ on Python 3
        return self.headline

    class Meta: 
        ordering = ['pub_date'] 


admin.py:
class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('blog', 'headline', 'slug', 'authors', 'body_text', 'pub_date', 'status', 'n_comments', 'n_pingbacks', 'rating' )
    filter_horizontal = ('authors',)
    raw_id_fields = ('blog',)
    prepopulated_fields = {"slug": ("headline",)}


```

## choices Field в Django

python manage.py makemigrations blog
python manage.py migrate 

## Создание функций для действий

Функции действий - это обычные функции, которые принимают три аргумента:
- Экземпляр класса ModelAdmin,
- Экземпляр класса HttpRequest, представляющий текущий запрос,
- Экземпляр класса QuerySet, содержащий набор объектов, которые выделил пользователь.

```
def make_published(modeladmin, request, queryset):
    queryset.update(status='1')

class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('blog', 'headline', 'slug', 'authors', 'body_text', 'pub_date', 'status', 'n_comments', 'n_pingbacks', 'rating' )
    filter_horizontal = ('authors',)
    raw_id_fields = ('blog',)
    prepopulated_fields = {"slug": ("headline",)}
    actions = [make_published]
```
сделаем ещё один необязательный, но полезный шаг и обеспечим действие “красивым” заголовком, который будет отображаться в интерфейсе администратора. По умолчанию, это действие будет отображено в списке действий как “Make published”, т.е. по имени функции, где символы подчёркивания будут заменены пробелами.

мы можем сделать лучше, предоставив функции make_published атрибут short_description:

```
def make_published(modeladmin, request, queryset):
    queryset.update(status='1')
make_published.short_description = "Mark selected stories as published"

class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('blog', 'headline', 'slug', 'authors', 'body_text', 'pub_date', 'status', 'n_comments', 'n_pingbacks', 'rating' )
    filter_horizontal = ('authors',)
    raw_id_fields = ('blog',)
    prepopulated_fields = {"slug": ("headline",)}
    actions = [make_published]
```

## Действия как методы ModelAdmin
Вышеприведённый пример показывает действие make_published, определённое в виде обычной функции. Это нормальный подход, но к нему есть претензии с точки зрения дизайна кода: так как действия связано с объектом Entry, то правильнее будет внедрить это действие в сам объект EntryAdmin.

```
def make_published(modeladmin, request, queryset):
    queryset.update(status='1')
make_published.short_description = "Mark selected stories as published"

class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('blog', 'headline', 'slug', 'authors', 'body_text', 'pub_date', 'status', 'n_comments', 'n_pingbacks', 'rating' )
    filter_horizontal = ('authors',)
    raw_id_fields = ('blog',)
    prepopulated_fields = {"slug": ("headline",)}
    actions = [make_published, 'make_draft']

    def make_draft(self, request, queryset):
        queryset.update(status='0')
    make_draft.short_description = "Mark selected stories as draft"

```

можем использовать self для вывода сообщения для пользователя
```
def make_published(modeladmin, request, queryset):
    queryset.update(status='1')
make_published.short_description = "Mark selected stories as published"

class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('blog', 'headline', 'slug', 'authors', 'body_text', 'pub_date', 'status', 'n_comments', 'n_pingbacks', 'rating' )
    filter_horizontal = ('authors',)
    raw_id_fields = ('blog',)
    prepopulated_fields = {"slug": ("headline",)}
    actions = [make_published, 'make_draft','make_unpublished']

    def make_draft(self, request, queryset):
        queryset.update(status='0')
    make_draft.short_description = "Mark selected stories as draft"

    def make_unpublished(self, request, queryset):
        rows_updated = queryset.update(status='2')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as unpublished." % message_bit)
    make_unpublished.short_description = "Mark selected stories as unpublished"

```
## Fortntend
### urls.py
```
from django.conf.urls import include, url

from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^posts/(?P<postslug>.*)/$', 'blog.views.view'),
    ]

```
### views.py
```

from django.shortcuts import render, render_to_response
from .models import Entry, Category

def index(request):

    posts_list = Entry.objects.order_by('headline')
    
    category_list = Category.objects.order_by('name')
        
    result = {'categories_list':category_list, 'posts_list':posts_list }

    return render(request,'blog/index.html',result)


def view(request, postslug):
    result = Entry.objects.get(slug=postslug)
    context = {'result': result}
    return render_to_response('blog/view.html', context)

```

### templates/blog/index.html
```
{% extends "base.html" %} 
{% load staticfiles %}
{% block title %} {{ block.super }} - SECTION NAME {% endblock %}

{% block content %} 

<h2>Index page</h2>
        {% if categories_list %}       
            <ul>
                {% for category in categories_list %}
                <li>{{ category.name }}</li>
                {% endfor %}
            </ul>
         

        {% else %}
            <strong>There are no categories present.</strong>
        {% endif %}

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

### templates/blog/view.html
```

{% extends "base.html" %}
{% block content %}
        <div id="singlepost">
                <p>{{ result.headline }}</p>
                <span>{{ result.pub_date|date:"SHORT_DATE_FORMAT" }} | 
                      {% for author in result.authors.all %}
                      {{ author|addslashes }} 
                      {% endfor %}
                </span>
                <p>
                {% autoescape off %}
                {{ result.body_text }} 
                {% endautoescape %}
                </p>
        </div>
{% endblock %}
```

