from _multiprocessing import send

from allauth.account.utils import user_email
from celery import shared_task
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.core.mail import send_mail

import news
from NewsPaper.celery import app
from news.models import Post, Category

@app.task
def send_news():
    for u in User.objects.all(user_email):
        if news in Post.object.all():
            send(subject='news', message="Вышла новая новость",from_email='teststudymail@yandex.ru',
                 recipient_list=['chudaevoleg@gmail.com'])

@shared_task
def send_new_news(**kwargs):
    User = get_user_model()
    user = User.objects.all().values_list("username")
    title = Post.objects.all().values('pk')
    text = Post.text
    cat = Category.objects.all().values_list('name', "subscribers")
    sub = Category.objects.all().values_list('name', flat=True)

    for n, m in cat:
        if m is not None:
            print('n:', n)
            print('m:', m)

            for c in sub:
                print('c:', c)
                if n == c:
                    send_mail(subject=f"{title}",
                              message=(f"Здравствуй,{user}. Новая статья в твоём любимом разделе! {c} \n Заголовок статьи: {title} \n Текст статьи: {text[:50]} \n Перейти на новость: http://127.0.0.1:8000/news/{title}"),
                              from_email='teststudymail@yandex.ru',
                              recipient_list=['chudaevoleg@gmail.com'],
                              )
