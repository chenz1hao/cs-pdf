from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from cs_pdf import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:b_id>', views.detail, name='detail'),
    path('download/<int:b_id>', views.download, name='download'),
    path('comment/', views.comment, name='comment'),
    path('s/', views.search, name='search'),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]