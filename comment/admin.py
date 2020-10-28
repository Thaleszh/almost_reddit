from django.contrib import admin
from comment.models import Comment


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'post', 'created_at', 'updated_at', 'content',)
    search_fields = ['title', 'author', 'post']
