from django.urls import path
from .views import main, about

urlpatterns = [
    path('about/', about, name='about'),

]
