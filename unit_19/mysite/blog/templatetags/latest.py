from django.template import Library, Node
from blog.models import Post
     
register = Library()
     
class LatestLinksNode(Node):
    def render(self, context):
        context['views'] = Post.objects.all()[:5]
        return ''
    
def get_latest_links(parser, token):
    return LatestLinksNode()
get_latest_links = register.tag(get_latest_links)