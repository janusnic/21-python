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

