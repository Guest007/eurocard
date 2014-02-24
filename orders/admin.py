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


class OrderForm(forms.ModelForm):
    name = forms.CharField()
    chip = forms.CharField()
    scratch = forms.CharField()
    magnet = forms.CharField()
    emboss = forms.CharField()
    uv = forms.CharField()
    print_num = forms.CharField()
    sign = forms.CharField()
    foil = forms.CharField()
    barcode = forms.CharField()
    indent = forms.CharField()
    material = forms.CharField()
    lamination = forms.CharField()
    color_front = forms.CharField()
    color_back = forms.CharField()

    class Meta:
        model = Orders
        readonly_fields = ['name', 'material']


    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].initial = self.instance.template.name
        self.fields['chip'].initial = self.instance.template.chip
        self.fields['scratch'].initial = self.instance.template.scratch
        self.fields['magnet'].initial = self.instance.template.magnet
        self.fields['emboss'].initial = self.instance.template.emboss
        self.fields['uv'].initial = self.instance.template.uv
        self.fields['print_num'].initial = self.instance.template.print_num
        self.fields['sign'].initial = self.instance.template.sign
        self.fields['foil'].initial = self.instance.template.foil
        self.fields['barcode'].initial = self.instance.template.barcode
        self.fields['indent'].initial = self.instance.template.indent
        self.fields['material'].initial = self.instance.template.material
        self.fields['lamination'].initial = self.instance.template.lamination
        self.fields['color_front'].initial = self.instance.template.color_front
        self.fields['color_back'].initial = self.instance.template.color_back


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['FIO', 'id', 'phone', 'email', 'draw']
    # ordering = ["category", 'published_at']
    list_filter = ['FIO', 'draw']

    form = OrderForm


class OrderTemplateAdmin(admin.ModelAdmin):
    model = OrderTemplate
    list_display = ['name', 'id', 'is_template', 'price']
    ordering = ["name", 'is_template', 'price']
    list_filter = ['name', 'is_template']


admin.site.register(Material, MaterialAdmin)
admin.site.register(Lamination, LaminationAdmin)
admin.site.register(Color, ColorAdmin)

admin.site.register(Coefficient, CoefficientAdmin)
admin.site.register(Modificators, ModificatorsAdmin)

admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderTemplate, OrderTemplateAdmin)
