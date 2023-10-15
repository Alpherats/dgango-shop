from django.urls import path
from .views import hello_view, show_items, edit_item

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('items/<int:id>/<int:days>/', show_items, name='show all items'),
    path('form/edit/<int:pk>/', edit_item, name='edit item in db'),
]
