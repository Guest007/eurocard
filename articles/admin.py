from django.contrib import admin
from articles.models import Category, Article
__author__ = 'guest007'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'category', 'published_at', 'is_active']
    ordering = ["category", 'published_at']
    list_filter = ['category', 'is_active']

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup/tinymce_setup.js',
        )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)