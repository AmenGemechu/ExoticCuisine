from django.contrib import admin
from .models import exotic_cuisine
from .models import Post
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin
# from djangosummernote.admin import SummernoteModelAdmin
# from .models import Bookings, Users, Test2, Test3
# from .models import Reservation


# Register your models here.
@admin.register(exotic_cuisine)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
