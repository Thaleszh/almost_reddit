from django.contrib import admin
from topic.models import Topic


# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'author', 'url_name', 'created_at', 'updated_at', 'description')
    search_fields = ['name', 'author', 'url_name']
