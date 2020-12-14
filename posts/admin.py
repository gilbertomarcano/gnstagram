from django.contrib import admin

from posts.models import Post

# Register your models here.

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Post admin
    """
    list_display = ('pk', 'user', 'profile', 'title', 'photo', 'created', 'modified')
