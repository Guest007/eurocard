# -*- coding: utf-8 -*-
from annoying.functions import get_object_or_None
from annoying.decorators import render_to
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from orders.models import OrderTemplate, Orders, Material, Lamination, Color
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django import http

__author__ = 'guest007'


def home(request):
    template_name = 'home1.html'
    return render_to_response(template_name,
                              {'draw': '500',
                              'materials': Material.objects.all(),
                              'lamination': Lamination.objects.all(),
                              'color_front': Color.objects.all().order_by('-id'),
                              'color_back': Color.objects.all().order_by('-id')},
                              context_instance=RequestContext(request))


@render_to()
def edit_order(request, pk, step=0):
    """Edit selected Order"""
    if step == 0:
        return http.HttpResponseRedirect('1/')
    order = get_object_or_404(Orders, pk=int(pk))
    templ = OrderTemplate.objects.get(id=order.template.id)
    return {"TEMPLATE": 'home1.html',
            "object": order,
            "templ": templ,
            'materials': Material.objects.all(),
            'lamination': Lamination.objects.all(),
            'color_front': Color.objects.all().order_by('-id'),
            'color_back': Color.objects.all().order_by('-id')}


# @render_to()
def nextstep_order(request, pk):
    """Final confirm of Order"""
    print "pk: ", pk
    order = get_object_or_404(Orders, pk=int(pk))
    templ = OrderTemplate.objects.get(id=order.template.id)
    result = {"object": order,
              "templ": templ,
              'material': Material.objects.get(id=templ.material),
              'lamination': Lamination.objects.get(id=templ.lamination),
              'color_front': Color.objects.get(id=templ.color_front),
              'color_back': Color.objects.get(id=templ.color_back)}
    return render_to_response('helpers.html', result,
        mimetype="application/xhtml+xml")


@csrf_protect
def save_order(request, step=1):
    """Save order with AJAX"""
    if request.method != "POST":
        result = {"result": "ERROR", "msg": "Wrong request method"}
        return http.HttpResponse(json.dumps(result),
                                 content_type="application/json")
    try:
        templ_id = int(request.POST.get("templ_id", 0))  # Если редактруем созданный заказ
    except (TypeError, ValueError):
        templ_id = 0

    user = request.POST.get("user", None)
    phone = request.POST.get("phone", None)
    email = request.POST.get("email", None)

    templ = get_object_or_None(OrderTemplate, pk=templ_id)  # Или получаем тело заказа или создаём новое (новый заказ)

    if templ is None:
        templ = OrderTemplate(name=(user if user else ''))  # Создаем тело заказа. Название - имя заказчика

    templ.material = Material(id=request.POST.get("materials", None))
    templ.color_back = Color(id=request.POST.get("color_back", None))
    templ.color_front = Color(id=request.POST.get("color_front", None))
    templ.lamination = Lamination(id=request.POST.get("lamination", None))
    templ.chip = request.POST.get("chip", False)
    templ.uv = request.POST.get("uv", False)
    templ.magnet = request.POST.get("magnet", False)
    templ.emboss = request.POST.get("emboss", False)
    templ.scratch = request.POST.get("scratch", False)
    templ.print_num = request.POST.get("print_num", False)
    templ.sign = request.POST.get("sign", False)
    templ.indent = request.POST.get("indent", False)
    templ.barcode = request.POST.get("barcode", False)
    templ.foil = request.POST.get("foil", False)

    draw = request.POST.get("draw", '500')  # количество в заказ

    templ.save()  # Сохраняем тело заказа для того, чтобы потом создать сам заказ
    if templ is None:  # Если тело заказа не сохранилось - возвращаем ошибку?
        result = {"result": "ERROR", "msg": "Please, correct the property type to get access to other tabs."}
        return http.HttpResponse(json.dumps(result),
                                 content_type="application/json")

    try:  # Проверяем, это новый заказ или редактируем созданный
        pk = int(request.POST.get("id", 0))
        print "ID of Order: ", pk
    except (TypeError, ValueError):
        pk = 0
    order = None
    if pk not in (None, 0):
        # Search existed objects
        order = get_object_or_None(Orders, pk=pk)
    if order is None:
        # Create new object
        order = Orders()

    order.template = OrderTemplate(id=templ.id)
    order.FIO = user
    order.draw = draw  # Количество
    order.cost = 0  # TODO: Пока просто пишем 0. ИСПРАВИТЬ!!!!
    order.email = email
    order.phone = phone
    # order.maket = ''  # TODO: Пока ничего не пишем. ИСПРАВИТЬ!!!

    order.save()
    print "ID of Order (order.id): ", order.id

    if step == '1':
        result = {"result": "OK", "id": order.id,
                  "msg": "Changes are saved. Don't forget to publish your advertisement!",
                  "url": reverse("edit-order", args=[order.id, 3])}
        return http.HttpResponse(json.dumps(result),
                                 content_type="application/json")
    else:
        result = {"result": "OK", "id": order.id, "msg": "This case 'else'",
                  "url": reverse("edit-order", args=[order.id, step])}
        return http.HttpResponse(json.dumps(result),
                                 content_type="application/json")

