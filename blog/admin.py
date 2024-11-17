from django.contrib import admin
from .models import Post
from .models import Comment

admin.site.register(Post)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    search_fields = ('text', 'author__username')
    list_filter = ('created_at',)