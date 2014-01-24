from django.shortcuts import render
from articles.models import Category, Article
from config.models import Settings

__author__ = 'guest007'

def prod(request):
    production = Article.objects.get(category__slug='prod')
    context = {'prod': production}
    return render(request, 'article.html', context)


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
    # production = Article.objects.get(category__slug='prod')
    # context = {'prod': production}
    return render(request, 'home.html')


def price(request):
    # production = Article.objects.get(category__slug='prod')
    # context = {'prod': production}
    return render(request, 'home.html')


def cooperation(request):
    # production = Article.objects.get(category__slug='prod')
    # context = {'prod': production}
    return render(request, 'home.html')


def contacts(request):
    about = Settings.objects.get(slug='about')
    context = {'about': about}
    return render(request, 'contacts.html', context)

