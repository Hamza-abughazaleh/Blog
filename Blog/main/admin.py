from django.contrib import admin
from main.models import Article, Like, Category


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_date', 'created_date', 'category')
    search_fields = ('title', 'id')
    list_display_links = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title', 'id')
    list_display_links = ('title',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'article_id')
    search_fields = ('user_id', 'article_id')
    list_display_links = ('id',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Like, LikeAdmin)
