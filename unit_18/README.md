## Модель Comment
```
from django.contrib.auth.models import User

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User)
    body = models.TextField()
    post = models.ForeignKey(Entry)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))


```
## Создаем миграции
```
 ./manage.py makemigrations blog

 ./manage.py migrate
```
## Создаем форму

```
from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment 
        exclude = ["post"]
```
## Редактируем админку
```

from .models import Category, Blog, Author, Entry, Comment 

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created"]

admin.site.register(Comment, CommentAdmin)
```
## Добавляем метод во views.py

```
from .models import Entry, Category, Comment

from blog.forms import CommentForm

from django.http import HttpResponseRedirect


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

```
## Изменяем метод 
```
def view(request, postslug):
    result = Entry.objects.get(slug=postslug)

    comments = Comment.objects.filter(post=result)

    context = {'result': result, "comments":comments,"form":CommentForm(), "user":request.user}
    return render(request,'blog/view.html', context)
```

## Создаем маршрут
blog/urls.py
```
from django.conf.urls import include, url

from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^posts/(?P<postslug>.*)/$', 'blog.views.view'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r"^add_comment/(?P<postslug>.*)/$", "blog.views.add_comment"),
    ]


```

## Изменяем представление
templates/blog/view.html
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
                        <!-- Comments  --> 
                  {% if comments %} 
                      <p>Comments:</p> 
                  {% endif %} 

                  {% for comment in comments %} 
                      <div class="comment"> 
                          <div class="time">{{ comment.created }} | {{ comment.author }}</div> 
                          <div class="body">{{ comment.body|linebreaks }}</div> 
                      </div> 
                  {% endfor %} 
                  {% if user.is_authenticated %} 
                  <div id="addc">Add a comment</div> 
                  <!-- Comment form  --> 
                      <form action="/blog/add_comment/{{ result.slug }}/" method="POST">{% csrf_token %} <!-- защита против CSRF атак -->
                          <div id="cform"> 
                  
                              <p>{{ form.body|linebreaks }}</p> 
                          </div> 
                          <div id="submit"><input type="submit" value="Submit"></div> 
                      </form> 
                      {% endif %}       
                  </div>

        </div>
{% endblock %}
```

## Счираем коментарии
```
           <!-- Comments  --> 
                  {% if comments %} 
                      <p>Comments: {{ comments|length }} </p> 
                  {% endif %} 

```

## Постраничное листание публикаций
Изменяем метод
```
from django.core.paginator import Paginator, InvalidPage, EmptyPage



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

```
## Изменяем представление
index.html
```
<!-- Next/Prev page links  --> 
      {% if posts_list.object_list and posts_list.paginator.num_pages > 1 %} 
        <div class="pagination" style="margin-top: 20px; margin-left: -20px; "> 
            <span class="step-links"> 
                {% if posts_list.has_previous %} 
                    <a href= "?page={{ posts_list.previous_page_number }}">newer entries &lt;&lt; </a> 
                {% endif %} 

                <span class="current"> 
                    &nbsp;Page {{ posts_list.number }} of {{ posts_list.paginator.num_pages }} 
                </span> 

                {% if posts_list.has_next %} 
                    <a href="?page={{ posts_list.next_page_number }}"> &gt;&gt; older entries</a> 
                {% endif %} 
            </span> 
        </div> 
       {% endif %}
```


## Постраничное листание коментариев
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

        

    context = {'result': result, "comments":comments,"form":CommentForm(), "user":request.user}
    return render(request,'blog/view.html', context)


```
## Представление 
```
                       <!-- Comments  --> 
                  {% if comments %} 
                      <p>Comments: {{ comments|length }} </p> 
                  {% endif %} 

                  {% for comment in comments %} 
                      <div class="comment"> 
                          <div class="time">{{ comment.created }} | {{ comment.author }}</div> 
                          <div class="body">{{ comment.body|linebreaks }}</div> 
                      </div> 
                  {% endfor %}

                    <!-- Next/Prev page links  --> 
      {% if comments.object_list and comments.paginator.num_pages > 1 %} 
        <div class="pagination" style="margin-top: 20px; margin-left: -20px; "> 
            <span class="step-links"> 
                {% if comments.has_previous %} 
                    <a href= "?page={{ comments.previous_page_number }}">newer entries &lt;&lt; </a> 
                {% endif %} 

                <span class="current"> 
                    &nbsp;Page {{ comments.number }} of {{ comments.paginator.num_pages }} 
                </span> 

                {% if comments.has_next %} 
                    <a href="?page={{ comments.next_page_number }}"> &gt;&gt; older entries</a> 
                {% endif %} 
            </span> 
        </div> 
       {% endif %}
```