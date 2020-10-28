from django.contrib import admin
from post.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'topic', 'created_at', 'updated_at', 'content',)
    search_fields = ['title', 'author', 'topic']
