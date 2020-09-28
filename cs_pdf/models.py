from django.db import models
from django.contrib.auth.models import User

from DjangoUeditor.models import UEditorField


class Category(models.Model):
    category_name = models.CharField('书籍分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name='类别排序')

    class Meta:
        verbose_name = '书籍类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class Book(models.Model):
    book_name = models.CharField('书籍名称', max_length=100)
    book_auth = models.CharField('作者', max_length=100)
    book_publish_date = models.DateTimeField('发行日期')
    book_brief = models.CharField('一句话简概', blank=True, null=True, max_length=100)
    book_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="类别", blank=True, null=True)
    book_download = models.FileField('下载链接', upload_to='pdf/')
    book_cover_img = models.ImageField(upload_to='cover_img/', verbose_name='封面图片', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    book_download_times = models.IntegerField(verbose_name='下载次数')
    book_thumb_up = models.IntegerField(verbose_name='点赞次数')
    book_detail = UEditorField('书籍介绍', width=800, height=500,
                    toolbars="full", imagePath="introimg/", filePath="introfile/",
                    upload_settings={"imageMaxSize": 1204000},
                    settings={}, command=None, blank=True
                    )
    book_size = models.FloatField(verbose_name='书籍大小')

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, verbose_name='评论所属书名', blank=True, null=True)
    comment_text = models.CharField('评论内容', max_length=500)
    comment_date = models.DateTimeField('评论日期')
    comment_user = models.CharField('评论人', max_length=30)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment_text


