from django.db import models
from utils import helpers
# Create your models here.

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
    # content = RichTextField()
    #widgets = models.ManyToManyField(Widget, null=True, blank=True)
    featured_image = models.ImageField(max_length=1024, null=True, blank=True, upload_to=get_page_file_name)
    related_slider = models.ForeignKey(Slider, null=True, blank=True)

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return self.__str__()
