from django.shortcuts import render
import logging
import random
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    num = random.randint(0, 100)
    logger.info(num)
    return HttpResponse(f"Hello, user {num}")


def main(request):
    logger.info(f'Someone {request.user} saw this page {request.path}')
    return HttpResponse(f"<h1>Main page</h1>"
                        f"<h2>About this project</h2>"
                        f"<p>Это заготовка под интернет магазин. Когда сделаем - тогда и сообщим =)</p>")


def about(request):
    logger.info(f'Someone {request.user} saw this page {request.path}')
    return HttpResponse(f"<h1>About page</h1>"
                        f"<h2>About me</h2>"
                        f"<p>Привет! Меня зовут Антон, мне 21 год, закончил университет и активно"
                        f"изучаю курсы от GeekBrains</p>")
