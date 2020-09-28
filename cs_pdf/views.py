import time
import geoip2.database

from urllib.parse import quote

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

from .models import Book, Tag, Comment, Category


def index(request):
    allBook = Book.objects.all()
    context = {'allBook': allBook}
    return render(request, 'index.html', context)


def detail(request, b_id):
    book = Book.objects.filter(pk=b_id).first()
    if book is not None:
        comments = Comment.objects.order_by('-comment_date').filter(book_id=b_id)
        context = {
            'book': book,
            'comments': comments,
        }
    else:
        context = {
            'tip': '不存在ID为' + str(b_id) + '的书籍'
        }
    return render(request, 'detail.html', context)


@csrf_protect
@require_http_methods(['POST'])
def download(request, b_id):
    book = Book.objects.filter(pk=b_id).first()
    if book is not None:
        response = HttpResponse(book.book_download, 'application/x-zip-compressed')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(
            quote(str(book.book_download).split('/')[1]))
        # 修改下载量数据库
        book.book_download_times = book.book_download_times + 1
        book.save()
        return response


@require_http_methods(['POST'])
def comment(request):
    Comment.objects.create(book_id=request.POST.get('b_id'),
                           comment_text=request.POST.get('comment_text'),
                           comment_date=time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())),
                           comment_user=getUserString(request))
    return HttpResponseRedirect(reverse('detail', args=[request.POST.get('b_id')]))


def getUserString(request):
    ip = request.META['REMOTE_ADDR']
    reader = geoip2.database.Reader('./static/GeoLite2-City.mmdb')
    response = reader.city('222.178.202.107')
    if str(ip).__eq__("127.0.0.1"):
        return "来自本地的用户"
    else:
        return "来自" + str(response.city.names['zh-CN']) + "的网友"


def search(request):
    search_text = request.POST.get('search_text')
    searchResult = Book.objects.filter(book_name__contains=search_text)
    if searchResult.count() != 0:
        context = {'allBook': searchResult}
    else:
        context = {
            'tip': '没有搜索结果'
        }
    return render(request, 'index.html', context)