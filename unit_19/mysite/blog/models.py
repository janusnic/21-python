from django.db import models
from django.contrib.auth.models import User
# Create your models here.

BLOG_ENTRY_STATUS = (
    ('0', 'Dratf'),
    ('1', 'Published'),
    ('2', 'Not Published'),
)

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug   = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):              # __str__ on Python 3
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    tagline = models.TextField()

    def __unicode__(self):              # __str__ on Python 3
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):              # __str__ on Python 3
        return u'%s %s' % (self.first_name, self.last_name)

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

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User)
    body = models.TextField()
    post = models.ForeignKey(Entry)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))
