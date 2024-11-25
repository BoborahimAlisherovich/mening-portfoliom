from django.contrib import admin
from .models import Article, Contact,Portfolio,Comment

admin.site.register(Contact)
admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","create_data","is_active"]
    list_filter = ["is_active"]


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=["title","create_data","is_active"]
    list_filter = ["is_active"]
