# -*- coding: utf-8 -*-
from django.db import models

__author__ = 'guest007'


class Settings(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    description = models.CharField(max_length=255, verbose_name="Description")
    content = models.CharField(blank=True, max_length=255, verbose_name="Value")
    richtext = models.TextField(blank=True, default="", verbose_name="RichText")

    def __unicode__(self):
        return self.name