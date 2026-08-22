from django.contrib import admin

from .models import Post, Comment

class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text', 'title']
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_enbale', 'publish_date', 'created_time', 'update_time']
    inlines = [CommentAdminInline]
    



admin.site.register(Post, PostAdmin)


