from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Настройка админки для модели BlogPost.
    """

    list_display = ("title", "is_published", "views_count", "created_at")

    list_filter = ("is_published", "created_at")

    search_fields = ("title", "content")

    prepopulated_fields = {"slug": ("title",)}

    readonly_fields = ("views_count", "created_at")
