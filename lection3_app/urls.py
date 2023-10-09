from django.urls import path
from .views import hello, HelloView, year_post, MonthPost, post_detail, index_view

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('post/<int:year>', year_post, name='post_year'),
    path('post/<int:year>/<int:month>', MonthPost.as_view(), name='post_month'),
    path('post/<int:year>/<int:month>/<slug:slug>', post_detail, name='post_detail'),
    path('', index_view, name='index'),
]
