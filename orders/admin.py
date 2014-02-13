# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from orders.models import Orders, OrderTemplate, Material, Lamination, Color, Coefficient, Modificators

__author__ = 'guest007'

class CoefficientAdmin(admin.ModelAdmin):
    list_display = ['name', 'numb', 'coeff']
    list_filter = ['name']
    list_editable = ['numb', 'coeff']


class ModificatorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cost']
    list_filter = ['name', 'slug']
    list_editable = ['cost']
    prepopulated_fields = {"slug": ("name",)}
    

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']
    list_filter = ['name']
    list_editable = ['cost']


class LaminationAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']
    list_filter = ['name']
    list_editable = ['cost']


class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_easy', 'cost']
    list_filter = ['name']
    list_editable = ['is_easy', 'cost']


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['FIO', 'phone', 'email', 'draw']
    # ordering = ["category", 'published_at']
    list_filter = ['FIO', 'draw']


class OrderTemplateAdmin(admin.ModelAdmin):
    model = OrderTemplate
    list_display = ['name', 'is_template', 'price']
    ordering = ["name", 'is_template', 'price']
    list_filter = ['name', 'is_template']


admin.site.register(Material, MaterialAdmin)
admin.site.register(Lamination, LaminationAdmin)
admin.site.register(Color, ColorAdmin)

admin.site.register(Coefficient, CoefficientAdmin)
admin.site.register(Modificators, ModificatorsAdmin)

admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderTemplate, OrderTemplateAdmin)
