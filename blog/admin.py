from django.contrib import admin
from .models import Article, Category, Tag
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_time', 'updated_time']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
