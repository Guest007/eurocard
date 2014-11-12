from django.shortcuts import render, render_to_response
from articles.models import Category, Article
from config.models import Settings

__author__ = 'guest007'

def prod(request):
    production = Article.objects.get(category__slug='prod')
    context = {'prod': production}
    return render(request, 'prod.html', context)


def clients(request):
    clnts = Article.objects.filter(category__slug='clients')
    context = {'clients': clnts}
    return render(request, 'article.html', context)


def news(request):
    news = Article.objects.filter(category__slug='news').filter(is_active=True)
    news_title = Settings.objects.get(slug='news-title')
    context = {'news': news, 'news_title': news_title}
    return render(request, 'article.html', context)


def newsitem(request, slug):
    try:
        news = Article.objects.filter(is_active=True).filter(category__slug='news').get(slug=slug)
        context = {'newsitem': news}
        response = render(request, 'article.html', context)
    except:
        context = {'newsitem': ''}
        response = render(request, '404.html', context)
    return response


def home(request):
    # production = Article.objects.get(category__slug='prod')
    # context = {'prod': production}
    return render(request, 'home.html')


def cards(request):
    about_ = Article.objects.filter(is_active=True).get(category__slug='cards')
    context = {'cards': about_}
    return render(request, 'article.html', context)


def price(request):
    price_ = Article.objects.get(category__slug='price')
    context = {'price': price_}
    return render(request, 'article.html', context)


def makets(request):
    makets_ = Article.objects.get(category__slug='makets')
    context = {'makets': makets_}
    return render(request, 'article.html', context)


def contacts(request):
    about = Settings.objects.get(slug='about')
    context = {'about': about}
    return render(request, 'contacts.html', context)


def pages(request, slug):
    page = ''
    try:
        page = Article.objects.filter(is_active=True).filter(category__slug='page').get(slug=slug)
        context = {'page': page}
        response = render(request, 'page.html', context)
    except:
        context = {'page': ''}
        response = render(request, '404.html', context)
    #context = {'page': page}
    return response # nder(request, 'page.html', context)

def card(request, slug):
    page = ''
    try:
        page = Article.objects.filter(is_active=True).filter(category__slug='card').get(slug=slug)
        context = {'page': page}
        response = render(request, 'page.html', context)
    except:
        #return render(request, 'home.html')
        context = {'page': ''}
        response = render(request, '404.html', context)
    #context = {'page': page}
    return response
