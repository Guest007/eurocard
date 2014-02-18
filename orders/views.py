# -*- coding: utf-8 -*-
from annoying.functions import get_object_or_None
from annoying.decorators import render_to
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from orders.models import OrderTemplate, Orders, Material, Lamination, Color, Modificators, Coefficient
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie, requires_csrf_token
from django import http
from django.http import HttpResponse


__author__ = 'guest007'


@csrf_protect
def fastform(request):
    price = Modificators.objects.all()
    coeff = Coefficient.objects.all()
    template_name = 'fast-form.html'
    return render_to_response(template_name,
                              {'modif': price,
                               'coeff': coeff,
                              'materials': Material.objects.all(),
                              'lamination': Lamination.objects.all(),
                              'color_front': Color.objects.filter(is_easy=False).order_by('-id'),
                              'color_back': Color.objects.filter(is_easy=False).order_by('-id')},
                              context_instance=RequestContext(request))


@csrf_protect
def easyform(request):
    price = Modificators.objects.all()
    coeff = Coefficient.objects.all()
    template_name = 'easy-form.html'
    return render_to_response(template_name,
                              {'modif': price,
                               'coeff': coeff,
                              'materials': Material.objects.all(),
                              'lamination': Lamination.objects.all(),
                              'color': Color.objects.filter(is_easy=True).order_by('-id')},
                              context_instance=RequestContext(request))


@csrf_exempt
def readyform(request):
    # price = Modificators.objects.all()
    # coeff = Coefficient.objects.all()
    templ = OrderTemplate.objects.filter(is_template=True)
    template_name = 'ready-form.html'
    return render_to_response(template_name,
                              {'templs': templ,
                               },
                              context_instance=RequestContext(request))


@render_to()
def edit_fast(request, pk, step=0):
    """Edit selected Order"""
    if step == 0:
        return http.HttpResponseRedirect('1/')
    order = get_object_or_404(Orders, pk=int(pk))
    templ = OrderTemplate.objects.get(id=order.template.id)
    return {"TEMPLATE": 'fast-form.html',
            "object": order,
            "templ": templ,
            'materials': Material.objects.all(),
            'lamination': Lamination.objects.all(),
            'color_front': Color.objects.all().order_by('-id'),
            'color_back': Color.objects.all().order_by('-id')}


@render_to()
def edit_easy(request, pk, step=0):
    """Edit selected Order"""
    if step == 0:
        return http.HttpResponseRedirect('1/')
    order = get_object_or_404(Orders, pk=int(pk))
    templ = OrderTemplate.objects.get(id=order.template.id)
    return {"TEMPLATE": 'easy-form.html',
            "object": order,
            "templ": templ,
            'materials': Material.objects.all(),
            'color_front': Color.objects.all().order_by('-id'),
            'color_back': Color.objects.all().order_by('-id')}


@csrf_protect
def nextstep_order(request, pk):
    """Final confirm of Order"""
    # print "pk: ", pk
    order = get_object_or_404(Orders, pk=int(pk))
    # print "And what??? ", order.template.id
    templ = OrderTemplate.objects.get(id=order.template.id)
    result = {"object": order,
              "templ": templ,
              'material': templ.material,
              'lamination': templ.lamination,
              'color_front': templ.color_front,
              'color_back': templ.color_back}
    return render_to_response('helpers.html', result,
        content_type="text/html; charset=utf-8")


@csrf_protect
def save_order(request, step=1):
    """Save order with AJAX"""
    if request.method != "POST":
        result = {"result": "ERROR", "msg": "Wrong request method"}
        return http.HttpResponse(json.dumps(result),
                                 content_type="application/json")

    try:
        id = int(request.POST.get("id", 0))  # Если редактруем созданный заказ
    except (TypeError, ValueError):
        id = 0

    user = request.POST.get("user", None)
    phone = request.POST.get("phone", None)
    email = request.POST.get("email", None)
    maket = request.POST.get("maket", None)

    if id != 0:
        templ_id = Orders.objects.get(id=id).template.id
        # print "templ_id: ", templ_id
    else:
        templ_id = 0

    templ = get_object_or_None(OrderTemplate, pk=templ_id)  # Или получаем тело заказа или создаём новое (новый заказ)
    # if templ:
    #     print "TEMPLATE IS PRESENT! ", templ.id
    if templ is None:
        templ = OrderTemplate(name=(user if user else ''))  # Создаем тело заказа. Название - имя заказчика

    if step > 20:
        print request.POST
        print request.POST.get("id", False)
        print request.POST.get("emboss", False)
    elif step > 10:
        # print "STEP more than 10"
        print request.POST
        templ.color_back = None  # Color(id=request.POST.get("color_back", None))
        templ.color_front = Color(id=(request.POST.get("colors", None)))
        # print "RAW color^ ", request.POST.get("colors", None)
        # print "COLOR: ", templ.color_front
        templ.material = Material(id=(request.POST.get("materials", None)))
        # print "MATERIAL: ", templ.material

        templ.chip = False  # request.POST.get("chip", False)
        templ.uv = False  # request.POST.get("uv", False)
        templ.magnet = (True if float(request.POST.get("magnet", False)) > 0 else False)
        templ.emboss = (True if float(request.POST.get("emboss", False)) > 0 else False)
        templ.scratch = (True if float(request.POST.get("scratch", False)) > 0 else False)
        templ.print_num = (True if float(request.POST.get("print_num", False)) > 0 else False)
        templ.sign = (True if float(request.POST.get("sign", False)) > 0 else False)
        templ.indent = (True if float(request.POST.get("indent", False)) > 0 else False)
        templ.barcode = (True if float(request.POST.get("barcode", False)) > 0 else False)
        templ.foil = (True if float(request.POST.get("foil", False)) > 0 else False)

    else:
        templ.color_back = Color(id=request.POST.get("color_back", None))
        templ.color_front = Color(id=request.POST.get("color_front", None))

        templ.material = Material(id=request.POST.get("materials", None))
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

    # print "material", templ.material
    # print "lamination", templ.lamination
    # print "chip", templ.chip
    # print "barcode", templ.barcode
    # print "foil", templ.foil

    draw = request.POST.get("count", 500)  # количество в заказ
    # print "DRAW: ", draw
    # print templ
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
    # print order.FIO
    order.draw = draw  # Количество
    # print order.draw
    order.cost = request.POST.get("sum", False)
    order.email = email
    # print order.email
    order.phone = phone
    # print order.phone
    order.maket = maket

    order.save()
    # print "ID of Order (order.id): ", order.id

    if step == '1':
        result = {"result": "OK", "id": order.id,
                  "msg": "Changes are saved. Don't forget to publish your advertisement!",
                  "url": reverse("edit-order", args=[order.id, 3])}
        return HttpResponse(json.dumps(result),
                                 content_type="application/json")
    elif step > 10:
        result = {"result": "OK", "id": order.id, "msg": "This case 'elif step > 10'",
                  "url": reverse("edit-easy", args=[order.id, step])}
        return HttpResponse(json.dumps(result),
                                 content_type="application/json")
    else:
        result = {"result": "OK", "id": order.id, "msg": "This case 'else'",
                  "url": reverse("edit-fast", args=[order.id, step])}
        return HttpResponse(json.dumps(result),
                                 content_type="application/json")




