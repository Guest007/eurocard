# -*- coding: utf-8 -*-
from django.db import models
__author__ = 'guest007'


class Coefficient(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование кэффициента")
    numb = models.IntegerField(verbose_name='От количества')
    coeff = models.CharField(max_length=100, verbose_name="Именение цены")

    class Meta:
        verbose_name = "Коэффициент"
        verbose_name_plural = "Коэффициенты"

    def __unicode__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование материала")
    cost = models.FloatField(blank=True, null=True, verbose_name="Стоимость за единицу")

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __unicode__(self):
        return self.name


class Lamination(models.Model):
    name = models.CharField(max_length=255, verbose_name="Вид ламинации")
    cost = models.FloatField(blank=True, null=True, verbose_name="Стоимость за единицу")

    class Meta:
        verbose_name = "Ламинирование"
        verbose_name_plural = "Ламинирование"

    def __unicode__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255, verbose_name="Цвет")
    cost = models.FloatField(blank=True, null=True, verbose_name="Стоимость за единицу")

    class Meta:
        verbose_name = "Цвета"
        verbose_name_plural = "Цвета"

    def __unicode__(self):
        return self.name


class OrderTemplate(models.Model):
    # constant fields
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=255, verbose_name="Описание")
    # constant boolean fields
    is_template = models.BooleanField(verbose_name="Это заготовка?")
    chip = models.BooleanField(verbose_name="карта с чипом")
    scratch = models.BooleanField(verbose_name="стираемая полоса")
    magnet = models.BooleanField(verbose_name="магнитная полоса")
    emboss = models.BooleanField(verbose_name="эмбоссирование")
    uv = models.BooleanField(verbose_name="печать УФ краской")
    print_num = models.BooleanField(verbose_name="печать номера")
    sign = models.BooleanField(verbose_name="полоса для подписи")
    foil = models.BooleanField(verbose_name="тиснение фольгой")
    barcode = models.BooleanField(verbose_name="печать штрих-кода")
    indent = models.BooleanField(verbose_name="идентная печать")
    # related fields
    material = models.ForeignKey(Material, verbose_name="Материал")
    lamination = models.ForeignKey(Lamination, verbose_name="Вид ламинации")
    color_front = models.ForeignKey(Color, related_name="color_front", verbose_name="Количество цветов на лицевой стороне")
    color_back = models.ForeignKey(Color, related_name="color_back", verbose_name="на обороте")
    # load file
    image = models.ImageField(upload_to="card/", blank=True, null=True, verbose_name="Образец")

    class Meta:
        verbose_name = "Шаблон заказа"
        verbose_name_plural = "Шаблоны заказов"

    def __unicode__(self):
        return self.name


class Orders(models.Model):
    # constant fields
    FIO = models.CharField(max_length=255, verbose_name="ФИО")
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    email = models.EmailField(verbose_name="E-mail")
    draw = models.IntegerField(default=1000, verbose_name="Тираж")
    cost = models.FloatField(blank=True, null=True, verbose_name="Стоимость за заказа")
    # load file
    maket = models.FileField(upload_to="maket/", blank=True, null=True, verbose_name="Мой макет (если есть)")
    # related fields
    template = models.ForeignKey(OrderTemplate, unique=True, verbose_name="Болванка заказа")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __unicode__(self):
        return self.FIO

