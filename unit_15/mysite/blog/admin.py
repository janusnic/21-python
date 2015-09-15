from django.contrib import admin

# Register your models here.
from .models import Category, Blog, Author, Entry 

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

def make_published(modeladmin, request, queryset):
    queryset.update(status='1')
make_published.short_description = "Mark selected stories as published"

class EntryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('blog', ('headline', 'slug'), 'authors', 'body_text', 'pub_date', 'status', 'n_comments', 'n_pingbacks', 'rating' )
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


admin.site.register(Author, AuthorAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Blog)

admin.site.register(Entry, EntryAdmin)