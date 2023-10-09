from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render


def hello(request):
    return HttpResponse('Hello world func')


class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello world class')


def year_post(request, year):
    text = ''
    ...
    return HttpResponse(f'Posts from {year} <br> {text}')


class MonthPost(View):
    def get(self, request, year, month):
        text = ''
        ...
        return HttpResponse(f'Posts from {year}/{month} <br> {text}')


def post_detail(request, year, month, slug):
    post = {
        'year': year,
        'month': month,
        'slug': slug,
        'title': 'Something',
        'content': 'About content'
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def index_view(request):
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {'name': 'Somebody',
               'my_list': my_list, }
    return render(request, 'lection3_app/index.html', context)
