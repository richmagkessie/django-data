from django.contrib import admin
from .models import Post, Comment, Category
# Register your models here.
class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
