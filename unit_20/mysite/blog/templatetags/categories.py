from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/cats.html')
def get_category_list():
    return {'cats': Category.objects.all()}