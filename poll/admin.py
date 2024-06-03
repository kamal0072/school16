from django.contrib import admin
from .models import MyUser, Page, Post, Song

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password']

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['id',  'page_name', 'page_cat', 'page_publish_date', 'myuser']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'auther', 'myuser']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'duration', 'singer_name', 'movie_name', 'sung_by']
