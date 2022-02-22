from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'published']
    list_filter = ['status', 'category', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
