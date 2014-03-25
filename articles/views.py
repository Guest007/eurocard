from django.shortcuts import render
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
    news = Article.objects.filter(category__slug='news')
    context = {'news': news}
    return render(request, 'article.html', context)


def newsitem(request, slug):
    print slug
    news = Article.objects.get(slug=slug)
    context = {'newsitem': news}
    return render(request, 'article.html', context)


def home(request):
    # production = Article.objects.get(category__slug='prod')
    # context = {'prod': production}
    return render(request, 'home.html')


def about(request):
    about_ = Article.objects.get(category__slug='about')
    context = {'about': about_}
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


