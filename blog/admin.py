from django.contrib import admin
from .models import Article, Contact
# Register your models here.

admin.site.register(Contact)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","create_data","is_active"]
    list_filter = ["is_active"]

