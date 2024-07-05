from django.contrib import admin
from .models import Article


# Register your models here.
class Article_Admin(admin.ModelAdmin):
    list_display = ("id", "title", "author")
    list_filter = ("author",)
    list_display_links = ("id", "title")


admin.site.register(Article, Article_Admin)
