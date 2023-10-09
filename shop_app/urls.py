from django.urls import path
from .views import hello_view, show_items

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('items/<int:id>/<int:days>/', show_items, name='show all items'),
]
