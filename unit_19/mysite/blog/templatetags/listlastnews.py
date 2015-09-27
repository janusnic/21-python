# -*- coding: UTF-8 -*-
from django import template
from blog.models import Entry, Comment
register=template.Library()
 
@register.inclusion_tag('blog/lastnews.html') # регистрируем тег и подключаем шаблон lastnews
def lastnews():
    return {
		'last3news': Entry.objects.filter(status='1')[:3],
	}
    