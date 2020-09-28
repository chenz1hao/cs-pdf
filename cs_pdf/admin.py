from django.contrib import admin

# Register your models here.
from cs_pdf.models import Category, Tag, Book, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'index')
    ordering = 'id',
    list_display_links = ('id', 'category_name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')
    ordering = 'id',
    list_display_links = ('id', 'tag_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'book_auth', 'book_publish_date', 'book_brief', 'book_download', 'book_cover_img', 'book_download_times', 'book_thumb_up', 'book_size')
    ordering = 'id',
    list_display_links = ('id', 'book_name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'comment_text', 'comment_date', 'comment_user')
    ordering = 'id',
    list_display_links = ('id',)