from django.contrib import admin
from django.contrib.admin.decorators import display
from django.db import models
from .models import Article, Commet
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter=("title",)
    list_display=("author","title","createdDate")
    search_fields=("title",)
    list_display_links=("author","title","createdDate")




    class Meta:
        model = Article

@admin.register(Commet)
class CommetAdmin(admin.ModelAdmin):
    class Meta:
        model = Commet
    



