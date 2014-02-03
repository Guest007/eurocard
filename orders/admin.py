# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from orders.models import Orders, OrderTemplate, Material, Lamination, Color, Coefficient

__author__ = 'guest007'

class CoefficientAdmin(admin.ModelAdmin):
    list_display = ['name', 'numb', 'coeff']
    list_filter = ['name']
    list_editable = ['numb', 'coeff']

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']
    list_filter = ['name']
    list_editable = ['cost']


class LaminationAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']
    list_filter = ['name']
    list_editable = ['cost']


class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']
    list_filter = ['name']
    list_editable = ['cost']


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['FIO', 'phone', 'email', 'draw']
    # ordering = ["category", 'published_at']
    list_filter = ['FIO', 'draw']
    # inlines = [TemplateLinkedInline]
    # fieldsets = (
    #     (u'Заказ', {
    #         'classes': ('grp-collapse grp-open'),
    #         'fields': ("FIO", "phone", "email", "draw", "cost", "maket")
    #     }),
    #     (u'Детально', {
    #         'classes': ('grp-collapse grp-open'),
    #         'fields': ('template', )
    #     })
    # )
    #
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "template":
    #         kwargs["queryset"] = OrderTemplate.objects.get(pk=self.template.pk)
    #     return super(OrdersAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class OrderTemplateAdmin(admin.ModelAdmin):
    model = OrderTemplate
    list_display = ['name', 'is_template', 'image']
    # ordering = ["category", 'published_at']
    list_filter = ['name', 'is_template']


admin.site.register(Material, MaterialAdmin)
admin.site.register(Lamination, LaminationAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderTemplate, OrderTemplateAdmin)
