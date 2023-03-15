from django.contrib import admin
from comments.models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment admin
    """
    list_display = ('pk', 'user', 'post', 'text', 'created', 'modified')
