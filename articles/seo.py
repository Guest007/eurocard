# -*- coding: utf-8 -*-
__author__ = 'guest007'
from rollyourown import seo

class EuroCardMetadata(seo.Metadata):
    title = seo.Tag(head=True, max_length=68, populate_from='Eurocard')
    description = seo.MetaTag(max_length=155)
    keywords = seo.KeywordTag()

    class Meta:
        verbose_name = "СЕО настройка для Еврокарт"
        verbose_name_plural = "СЕО настройки для Еврокарт"

    class HelpText:
        title = "Этот текст будет виден в заголовке окна и влияет на результат поисковой выдачи"
        description = 'Описание содержимого страницы/сайта. Влияет на результат поисковой выдачи'
        keywords = "Разделенный запятыми список слови или фраз, описывающий содержимое страницы"