# -*- coding: utf-8 -*-
from django import forms
from orders.models import OrderTemplate, Orders, Material, Lamination, Color
from django.forms.formsets import formset_factory

class TemplOrderForm(forms.ModelForm):
    barcode = forms.BooleanField()

    class Meta:
        model = OrderTemplate
        fields = ['name', 'is_template', 'price', 'barcode']

# TOrderFormSet = formset_factory(TemplOrderForm)


class OrderForm(forms.ModelForm):
    chip = forms.BooleanField()
    scratch = forms.BooleanField()
    magnet = forms.BooleanField()
    emboss = forms.BooleanField()
    uv = forms.BooleanField()
    print_num = forms.BooleanField()
    sign = forms.BooleanField()
    foil = forms.BooleanField()
    barcode = forms.BooleanField()
    indent = forms.BooleanField()
    # price = forms.FloatField()

    # related fields
    material = forms.ModelChoiceField(queryset=Material.objects.all())
    lamination = forms.ModelChoiceField(queryset=Lamination.objects.all())
    color_front = forms.ModelChoiceField(queryset=Color.objects.all())
    color_back = forms.ModelChoiceField(queryset=Color.objects.all())
    # load file
    # image = forms.ImageField(upload_to="card/", blank=True, null=True, verbose_name="Образец")

    class Meta:
        model = Orders
        # fields = ['draw']

