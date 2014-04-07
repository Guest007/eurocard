# -*- coding: utf-8 -*-
import os
from annoying.functions import get_object_or_None
from annoying.decorators import render_to
import datetime
import time
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from orders.models import OrderTemplate, Orders, Material, Lamination, Color, Modificators, Coefficient
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django import http
from django.http import HttpResponse
from mailshelf import messages
from config.models import Settings

__author__ = 'guest007'


@csrf_protect
def fastform(request):
    price = Modificators.objects.all()
    coeff = Coefficient.objects.all()
    try:
        material_def = Settings.objects.get(slug='material').content
    except:
        material_def = 0
    try:
        lam_def = Settings.objects.get(slug='lamination').content
    except:
        lam_def = 0
    try:
        color_def = Settings.objects.get(slug='fullcolor').content
    except:
        color_def = 0
    material = Material.objects.get(id=1)  # захардкодили Пластик
    color = Color.objects.filter(is_easy=True).get(name='4+4')  # захардкодили Color
    template_name = 'fast-form.html'
    return render_to_response(template_name,
                              {'modif': price,
                               'coeff': coeff,
                              'materials': material,
                              'md': material_def,
                              'ld': lam_def,
                              'cd': color_def,
                              'lamination': Lamination.objects.all().order_by('-id'),
                              'color': color
                              },
                              context_instance=RequestContext(request))


@csrf_protect
def easyform(request):
    price = Modificators.objects.all()
    coeff = Coefficient.objects.all()
    try:
        material_def = Settings.objects.get(slug='material').content
    except:
        material_def = 0
    try:
        lam_def = Settings.objects.get(slug='lamination').content
    except:
        lam_def = 0
    try:
        color_def = Settings.objects.get(slug='fullcolor').content
    except:
        color_def = 0
    tips = {}
    for i in Settings.objects.filter(slug__startswith='tip-'):
        tips[i.slug] = [i.content, i.richtext]
    material = Material.objects.get(id=1)  # захардкодили Пластик
    color = Color.objects.filter(is_easy=True).get(name='4+4')  # захардкодили Color
    template_name = 'easy-form.html'
    return render_to_response(template_name,
                              {'modif': price,
                               'coeff': coeff,
                              'materials': material,
                              'tips': tips,
                              'md': material_def,
                              'ld': lam_def,
                              'cd': color_def,
                              'lamination': Lamination.objects.all().order_by('-id'),
                              'color': color
                              },
                              context_instance=RequestContext(request))


@csrf_exempt
def readyform(request):
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


@render_to()
def edit_templ(request, pk, step=0):
    """Edit selected Order"""
    if step == 0:
        return http.HttpResponseRedirect('1/')
    order = get_object_or_404(Orders, pk=int(pk))
    templ = OrderTemplate.objects.get(id=order.template.id)
    return {"TEMPLATE": 'ready-form.html',
            "object": order,
            "templ": templ}


@csrf_protect
def nextstep_order(request, pk):
    """Final confirm of Order"""
    order = get_object_or_404(Orders, pk=int(pk))
    templ = OrderTemplate.objects.get(id=order.template.id)
    result = {"object": order,
              "templ": templ,
              'material': templ.material,
              'lamination': templ.lamination,
              'color_front': templ.color_front,
              'color_back': templ.color_back}
    return render_to_response('helpers.html', result,
                              content_type="text/html; charset=utf-8",
                              context_instance=RequestContext(request))


@csrf_exempt
def ajax_save(request):
    result = []
    if len(request.FILES) == 1:
        upload = request.FILES.values()[0]
    else:
        raise http.Http404("Bad upload")
    filename = upload.name
    ffile = save_uploaded_file_new(upload, filename)
    if ffile is not None and ffile is not False:
        result.append(ffile)
    else:
        result.append({"error": "Error save file"})
    response = http.HttpResponse('<input type="hidden" id="fd" name="maket" value="' + ffile + '"></input>',
                                 content_type="text/html; charset=utf-8")
    return response


def save_uploaded_file_new(uploaded, fname):
    """Just save uploaded file"""
    ufile = None
    try:
        split = fname.rsplit('.', 1)
        file = uploaded
        dt = datetime.datetime.now()
        name = '%s-%s' % (split[0], (int(time.mktime(dt.timetuple()))))
        name = 'maket/' + name + '.' + split[1]
        path = default_storage.save(name, ContentFile(file.read()))
    except Exception as e:
        print e
    if os.path.exists(name.decode('utf-8')):
        os.unlink(name.decode('utf-8'))
    return path


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

    else:
        templ_id = 0

    templ = get_object_or_None(OrderTemplate, pk=templ_id)  # Или получаем тело заказа или создаём новое (новый заказ)

    if templ is None:
        templ = OrderTemplate(name=(user if user else ''))  # Создаем тело заказа. Название - имя заказчика

    if int(step) > 10:
        # print request.POST
        templ.color_back = None  # Color(id=request.POST.get("color_back", None))
        templ.color_front = Color(id=(request.POST.get("colors", None)))

        templ.material = Material(id=(request.POST.get("materials", None)))

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
        templ.chip = (True if float(request.POST.get("chip", False)) > 0 else False)
        templ.uv = (True if float(request.POST.get("uv", False)) > 0 else False)
        templ.magnet = (True if float(request.POST.get("magnet", False)) > 0 else False)
        templ.emboss = (True if float(request.POST.get("emboss", False)) > 0 else False)
        templ.scratch = (True if float(request.POST.get("scratch", False)) > 0 else False)
        templ.print_num = (True if float(request.POST.get("print_num", False)) > 0 else False)
        templ.sign = (True if float(request.POST.get("sign", False)) > 0 else False)
        templ.indent = (True if float(request.POST.get("indent", False)) > 0 else False)
        templ.barcode = (True if float(request.POST.get("barcode", False)) > 0 else False)
        templ.foil = (True if float(request.POST.get("foil", False)) > 0 else False)

    draw = request.POST.get("count", None)  # количество в заказ
    if not draw:
        draw = 0

    templ.save()  # Сохраняем тело заказа для того, чтобы потом создать сам заказ
    if templ is None:  # Если тело заказа не сохранилось - возвращаем ошибку?
        result = {"result": "ERROR", "msg": "Please, correct the property type to get access to other tabs."}
        return http.HttpResponse(json.dumps(result),
                                 content_type="application/json")

    try:  # Проверяем, это новый заказ или редактируем созданный
        pk = int(request.POST.get("id", 0))
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
    order.cost = request.POST.get("sum", False)
    order.email = email
    order.phone = phone
    order.maket = maket

    order.save()

    if step == '1':
        result = {"result": "OK", "id": order.id,
                  "msg": "Changes are saved",
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


@csrf_exempt
def save_order1(request, step=1):
    """Save order from template with AJAX"""
    if request.method != "POST":
        result = {"result": "ERROR", "msg": "Wrong request method"}
        return http.HttpResponse(json.dumps(result),
                                 content_type="application/json")

    try:
        id = int(request.POST.get("id", 0))  # Если редактруем созданный заказ
    except (TypeError, ValueError):
        id = 0

    draw = request.POST.get("count", None)  # количество в заказ
    if not draw:
        draw = 0

    time = datetime.datetime.now()

    templ = OrderTemplate.objects.get(id=id)
    price = templ.price

    templ.pk = None

    templ.is_template = False
    templ.name = str(time) + " " + templ.name
    templ.price = None
    templ.save()  # взяли шаблон по id, обрали признак шаблона и скопировали.

    order = Orders(template=templ)

    order.draw = draw
    order.cost = float(draw) * float(price)

    order.save()  # привязали заказ к шаблону, посчитали цену, записали. Теперь нужны остальные данные и всё.

    step = 2


    result = {"result": "OK", "id": order.id,
              "msg": "Changes are saved",
              "url": reverse("edit-templ", args=[order.pk, 3])}
    return HttpResponse(json.dumps(result),
                                 content_type="application/json")



@csrf_exempt
def callback(request):
    name = request.POST.get('fio', False)
    phone = request.POST.get('phone', False)
    message = request.POST.get('message', '')
    time = datetime.datetime.now()
    if not phone or len(phone) < 3:
        return http.HttpResponse('Without Phone', content_type="text/html; charset=utf-8")

    email = Settings.objects.get(slug='callback-mail')

    try:
        messages.CALL_BACK.send(email.content,
                                   **{
                                       'name': name,
                                       'phone': phone,
                                       'message': message,
                                       'time': time
                                   })
    except:
        pass

    response = http.HttpResponse('OK', content_type="text/html; charset=utf-8")
    return response


@csrf_exempt
def finish(request):
    time = datetime.datetime.now()

    payment_status = request.POST.get('payment_status', False)
    raschet = request.POST.get('raschet', False)
    order = request.POST.get('id', False)

    obj = Orders.objects.get(id=int(order))
    if not obj.FIO:
        obj.FIO = request.POST.get('name', False)
        obj.email = request.POST.get('email', False)
        obj.phone = request.POST.get('phone_', False)
        obj.save()


    items = {
        u'с чипом': (u'да' if obj.template.chip else u'нет'),
        u'скрэтч панель': (u'да' if obj.template.scratch else u'нет'),
        u'магнитная полоса': (u'да' if obj.template.magnet else u'нет'),
        u'эмбоссирование': (u'да' if obj.template.emboss else u'нет'),
        u'ультрафиолетовые чернила': (u'да' if obj.template.uv else u'нет'),
        u'печатный номер': (u'да' if obj.template.print_num else u'нет'),
        u'полоса для подписи': (u'да' if obj.template.sign else u'нет'),
        u'фольгирование': (u'да' if obj.template.foil else u'нет'),
        u'штрихкод': (u'да' if obj.template.barcode else u'нет'),
        u'индентная печать': (u'да' if obj.template.indent else u'нет'),
        u'Материал': obj.template.material,
        u'Ламинирование': obj.template.lamination,
        u'Количество цветов лицевой стороны (или комбинация)': obj.template.color_front,
        u'Количество цветов обратной стороны': obj.template.color_back
    }

    mail_content = {
        'fio': obj.FIO,
        'id': obj.id,
        'phone': obj.phone,
        'email': obj.email,
        'draw': obj.draw,
        'cost': obj.cost,
        'maket': obj.maket,
        'items': items,
        'payment_status': (u'Юр.лицо' if payment_status == 'u' else u'Физ.лицо'),
        'raschet': (u'Безналичный' if raschet == '2' else u'Наличный'),
        'time': time
    }

    email = Settings.objects.get(slug='order-mail').content

    try:
        messages.ORDER_TO_CLIENT.send(obj.email,
                                      **mail_content)
        # print "SENT"
    except:
        pass

    try:
        messages.ORDER_TO_MANAGER.send(email,
                                       **mail_content)
        # print "SENT"
    except:
        pass

    response = http.HttpResponse('OK', content_type="text/html; charset=utf-8")
    return response