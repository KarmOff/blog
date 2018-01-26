from django.contrib import admin
from blog.models import *

class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments)
