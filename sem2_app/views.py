from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render


# Create your views here.

def main(request):
    return HttpResponse(f"<h1>Main page</h1>"
                        f"<h2>About this project</h2>"
                        f"<p>Это заготовка под интернет магазин. Когда сделаем - тогда и сообщим =)</p>")


def about(request):
    context = {'name': 'Tony'}
    return render(request, 'sem2_app/about.html', context)
