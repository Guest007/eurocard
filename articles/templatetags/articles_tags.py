# -*- coding: utf-8 -*-
from django import template
from articles.models import Category, Article

register = template.Library()

__author__ = 'guest007'


def active_news_block(context, count=3):
    query = Article.objects.filter(is_active=True,
                                   category__slug='news')\
                   .order_by("-published_at")
    query = query[:count]  # на всякий случай - вдруг больше отметили
    return {"objects": query, "STATIC_URL": context["STATIC_URL"]}

register.inclusion_tag("tags/tag.active_news_block.html",
                       takes_context=True)(active_news_block)