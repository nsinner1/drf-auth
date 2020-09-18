from django.urls import path, include
from .views import BookList, BookDetail
from django.contrib import admin

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('<int:pk>', BookDetail.as_view(), name='book_detail'),
    path('api-auth/', include('rest_framework.urls')),
]

