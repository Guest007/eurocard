# -*- coding: utf-8 -*-
from django.db import models
__author__ = 'guest007'


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name="Категория")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug", db_index=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class Article(models.Model):

    category = models.ForeignKey(Category, verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    annotation = models.TextField(blank=True, default='', verbose_name='Annotation')
    content = models.TextField(blank=True, default="", verbose_name="Content")
    published_at = models.DateField(auto_now_add=True, verbose_name="Date of publication")
    is_active = models.BooleanField(default=False, db_index=True, verbose_name="Active")
    logo = models.ImageField(upload_to='logo/', blank=True, null=True, verbose_name="Logo")
    card = models.ImageField(upload_to='card/', blank=True, null=True, verbose_name="Изображение карты или изображение для 'Акции и Спецпредложения'")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __unicode__(self):
        return self.title

