from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from allauth.account.admin import EmailAddress
from django.contrib.auth.decorators import login_required
from .models import product, order, favourite, userdetail
from django.contrib import messages
import ast
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()
from .tests import addprods


#####################---------- Start HelpFull Functions ----------#####################
def ordersdef(request):
    # ordersed = order.objects.filter(user=request.user, status='INCART')
    # return ordersed if ordersed else None
    if order.objects.filter(user=request.user, status='INCART').exists():
        ordersed = ast.literal_eval(order.objects.filter(user=request.user, status='INCART')[0].prodJson)
        return ordersed
    return None


def favdef(request):
    fav = [favourite.objects.filter(user=request.user, added=values.added)[0].added for values in favourite.objects.filter(user=request.user)]
    return fav if fav else None


def proddef():
    prod = product.objects.all().order_by('-id')
    return prod if prod else None

def branddef():
    brands = product.objects.values_list('brand', flat=True).distinct()
    return brands if brands else None

def categorydef():
    categorys = product.objects.values_list('category', flat=True).distinct()
    return categorys if categorys else None

def colordef():
    colors = product.objects.values_list('color', flat=True).distinct()
    return colors if colors else None


def checkuser(request):
    dicts = {}
    if EmailAddress.objects.filter(email=request.user.email).exists():
        if (request.user.is_verified or EmailAddress.objects.filter(email=request.user.email)[0].verified) and not request.user.is_staff:
            return dicts
        elif (request.user.is_verified or EmailAddress.objects.filter(email=request.user.email)[0].verified) and request.user.is_staff:
            dicts['url'] = '/staff/pending/'
            return dicts
        else:
            messages.add_message(request, messages.ERROR, 'Your Account Is Not Verified Yet Please Check Your Mail Or Contact Website Owner')
            dicts['url'] = '/signin/'
            return dicts
    elif not EmailAddress.objects.filter(email=request.user.email).exists():
        if (request.user.is_verified) and not request.user.is_staff:
            return dicts
        elif (request.user.is_verified) and request.user.is_staff:
            dicts['url'] = '/staff/pending/'
            return dicts
        else:
            messages.add_message(request, messages.ERROR, 'Your Account Is Not Verified Yet Please Check Your Mail Or Contact Website Owner')
            dicts['url'] = '/signin/'
            return dicts
    else:
        messages.add_message(request, messages.ERROR, 'Your Account Is Not Verified Yet Please Check Your Mail Or Contact Website Owner')
        dicts['url'] = '/signin/'
        return dicts


def idtotal(x, value):
    price = product.objects.filter(id=x)[0].priceByBox
    piece = product.objects.filter(id=x)[0].peicePerBox
    return round(round(price / piece, 3) * value, 3)
#####################---------- End HelpFull Functions ----------#####################








#####################---------- Start Index Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def index(request):
    # addprods()
    dicts = checkuser(request)
    if not 'url' in dicts:
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            'products': proddef(),
        }
        return render(request, 'index.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Index Function ----------#####################






#####################---------- Start Cart Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def cart(request):
    dicts = checkuser(request)
    if not 'url' in dicts:
        orders = ordersdef(request)
        if not order.objects.filter(user=request.user, status='INCART').exists():
            return render(request, 'customer/order/cart.html', {
                'orders': ordersdef(request),
                'favourite': favdef(request),
                'brands': branddef(),
                "categorys": categorydef(),
                'colors': colordef(),
                })
        orders = order.objects.filter(user=request.user, status='INCART')
        orderJson = ast.literal_eval(orders[0].prodJson)
        prodQuan = []
        products = []
        totals = []
        perproducts = []
        if orders:
            for key, value in orderJson.items():
                products.append(product.objects.filter(id=key)[0])
                totals.append(idtotal(key, value))
                prodQuan.append(value)
                perproducts.append(round(product.objects.filter(id=key)[0].priceByBox / product.objects.filter(id=key)[0].peicePerBox, 3))
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            'products': products,
            'prodQuan': prodQuan,
            "perproducts": perproducts,
            'totals': totals,
        }
        return render(request, 'customer/order/cart.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Cart Function ----------#####################






#####################---------- Start Product Page Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def productspage(request):
    dicts = checkuser(request)
    if not 'url' in dicts:
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            'products': proddef(),
            }
        return render(request, 'customer/products.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Product Page Function ----------#####################









#####################---------- Start Brand Page Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def brandspage(request, brand):
    dicts = checkuser(request)
    if not 'url' in dicts:
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            'products': product.objects.filter(brand=brand),
            'brand': brand,
            }
        return render(request, 'customer/brand.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Brand Page Function ----------#####################






#####################---------- Start Category Page Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def categoryspage(request, category):
    dicts = checkuser(request)
    if not 'url' in dicts:
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            'products': product.objects.filter(category=category),
            'category': category,
            }
        return render(request, 'customer/category.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Category Page Function ----------#####################





#####################---------- Start Color Page Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def colorspage(request, color):
    dicts = checkuser(request)
    if not 'url' in dicts:
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            'products': product.objects.filter(color=color),
            'color': color,
            }
        return render(request, 'customer/color.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Category Page Function ----------#####################






#####################---------- Start Checkout Page Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def checkout(request):
    dicts = checkuser(request)
    if not 'url' in dicts:
        if userdetail.objects.filter(user=request.user).exists():
            userdetails = userdetail.objects.filter(user=request.user)[0]
        else:
            userdetails = None
        
        if order.objects.filter(user=request.user, status='INCART').exists():
            total = order.objects.filter(user=request.user, status='INCART')[0].total
        else:
            total = None
        
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            "userdetail": userdetails,
            "total": total,
            }
        return render(request, 'customer/checkout.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Checkout Page Function ----------#####################









#####################---------- Start Pending Cart Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def pending(request):
    dicts = checkuser(request)
    if not 'url' in dicts:
        if order.objects.filter(user=request.user, status='PENDING').exists():
            orderdetails = order.objects.filter(user=request.user, status='PENDING').order_by("-id")
        else:
            orderdetails = None
        if order.objects.filter(user=request.user, status='INCART').exists():
            change = order.objects.filter(user=request.user, status='INCART')
        else:
            change = None
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            "orderdetails": orderdetails,
            "change": change,
        }
        return render(request, 'customer/order/pending.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Pending Cart Function ----------#####################









#####################---------- Start Processing Cart Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def processing(request):
    dicts = checkuser(request)
    if not 'url' in dicts:
        if order.objects.filter(user=request.user, status='PROCESSING').exists():
            orderdetails = order.objects.filter(user=request.user, status='PROCESSING').order_by("-id")
        else:
            orderdetails = None
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            "orderdetails": orderdetails,
        }
        return render(request, 'customer/order/processing.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Processing Cart Function ----------#####################









#####################---------- Start Completed Cart Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def completed(request):
    dicts = checkuser(request)
    if not 'url' in dicts:
        if order.objects.filter(user=request.user, status='COMPLETED').exists():
            orderdetails = order.objects.filter(user=request.user, status='COMPLETED').order_by("-id")
        else:
            orderdetails = None
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            "orderdetails": orderdetails,
        }
        return render(request, 'customer/order/completed.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Completed Cart Function ----------#####################









#####################---------- Start Cancelled Cart Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def cancelled(request):
    dicts = checkuser(request)
    if not 'url' in dicts:
        if order.objects.filter(user=request.user, status='CANCELLED').exists():
            orderdetails = order.objects.filter(user=request.user, status='CANCELLED').order_by("-id")
        else:
            orderdetails = None
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            "orderdetails": orderdetails,
        }
        return render(request, 'customer/order/cancelled.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Cancelled Cart Function ----------#####################








#####################---------- Start Favourite Products Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def favourites(request):
    dicts = checkuser(request)
    if not 'url' in dicts:
        products = []
        if favourite.objects.filter(user=request.user).exists():
            favdetails = favourite.objects.filter(user=request.user)
            for fav in favdetails:
                products.append(product.objects.get(id=fav.added))
        else:
            favdetails = None
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'colors': colordef(),
            'products': products,
        }
        return render(request, 'customer/favourite.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Favourite Products Function ----------#####################






#####################---------- Start Change Order Status Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def changepage(request, id):
    dicts = checkuser(request)
    if not 'url' in dicts:
        if order.objects.filter(user=request.user, id=id).exists():
            orderesed = order.objects.get(user=request.user, id=id)
            orderesed.status = "INCART"
            orderesed.save()
            userdetails = userdetail.objects.get(user=request.user)
            userdetails.total = round(float(userdetails.total) - float(orderesed.total), 3)
            userdetails.save()
            return redirect('/cart/')
        return redirect('/cart/pending/')
    else:
        return redirect(dicts['url'])
#####################---------- End Change Order Status Function ----------#####################













#---------------------------------On Json Call Functions---------------------------------#
#####################---------- Start Add Cart Function ----------#####################
def addcart(request):
    prodJson = {}
    prodId = request.POST.get('id')
    stock = int(product.objects.filter(id=prodId)[0].peicePerBox)
    prodquan = int(request.POST.get('quantity')) if not 'quantityb' in request.POST else int(int(request.POST.get('quantityb')) * int(stock))
    if not order.objects.filter(user=request.user, status='INCART').exists():
        prodJson[prodId] = prodquan
        createorder = order.objects.create(user=request.user, prodJson=prodJson)
        createorder.save()
        lenth = len(ordersdef(request)) if ordersdef(request) != None else 0
        prodtotal = idtotal(prodId, prodquan)
        return JsonResponse({"len": lenth, "pp" : prodtotal}, safe=False)
    else:
        editorder = order.objects.filter(user=request.user, status='INCART')[0]
        prodJson = ast.literal_eval(editorder.prodJson)
        prodJson[prodId] = prodquan
        editorder.prodJson = prodJson
        editorder.save()
        lenth = len(ordersdef(request)) if ordersdef(request) != None else 0
        prodtotal = idtotal(prodId, prodquan)
        return JsonResponse({"len": lenth, "pp" : prodtotal}, safe=False)
#####################---------- End Add Cart Function ----------#####################





#####################---------- Start Product From Cart Delete Function ----------#####################
def delete(request, id):
    orders = order.objects.get(user=request.user, status='INCART')
    jsons = ast.literal_eval(orders.prodJson)
    if len(jsons) > 1:
        if str(id) in jsons.keys():
            del jsons[str(id)]
            orders.prodJson = jsons
            orders.save()
    else:
        orders.delete()
    lenth = len(ordersdef(request)) if ordersdef(request) != None else 0
    return JsonResponse({'data': True, "len": lenth}, safe=False)
#####################---------- End Product From Cart Delete Function ----------#####################







#####################---------- Start Add Fav Function ----------#####################
def addtofav(request):
    data = int(request.POST.get('id'))
    if not favourite.objects.filter(user=request.user, added=int(data)).exists():
        favourite.objects.create(user=request.user, added=int(data))
        return JsonResponse({"data": True}, safe=False)
    else:
        favourite.objects.filter(user=request.user, added=int(data)).delete()
        return JsonResponse({"data": False}, safe=False)
#####################---------- End Add Fav Function ----------#####################



#####################---------- Start Add Fav Function ----------#####################
def total(request):
    if order.objects.filter(user=request.user, status='INCART').exists():
        totals = []
        withoutpercent = []
        if len(list(order.objects.filter(user=request.user, status='INCART'))) > 1:
            prodId = order.objects.filter(user=request.user, status='INCART')[0].id
            orders = order.objects.get(user=request.user, status='INCART', id=prodId)
        else:
            orders = order.objects.get(user=request.user, status='INCART')
        prodJson = ast.literal_eval(orders.prodJson)
        for key, value in prodJson.items():
            if product.objects.get(id=key).discount:
                totals.append(idtotal(key, value))
            else:
                withoutpercent.append(idtotal(key, value))
        carttotal = round(sum(totals), 3)
        if userdetail.objects.filter(user=request.user).exists():
            percent = userdetail.objects.filter(user=request.user)[0].OnCreditPercentage
        else:
            percent = 0
        saved = round((float(carttotal) / 100 * float(percent)), 3)
        total = round(float(carttotal) - float(saved), 3)
        orders.carttotal = round(float(carttotal) + float(sum(withoutpercent)), 3)
        orders.percent = percent
        orders.saved = round(float(saved) + float(sum(withoutpercent)), 3)
        orders.total = round(float(total) + float(sum(withoutpercent)), 3)
        orders.save()
        return JsonResponse({"data": True,
        "carttotal": round(float(carttotal) + float(sum(withoutpercent)), 3),
        'percent': percent,
        "save": saved,
        "total": round(float(total) + float(sum(withoutpercent)), 3)},
        safe=False)

    return JsonResponse({"data": False}, safe=False)
#####################---------- End Add Fav Function ----------#####################








def changetotal(request):
    totals = []
    withoutpercent = []
    if len(list(order.objects.filter(user=request.user, status='INCART'))) > 1:
        prodId = order.objects.filter(user=request.user, status='INCART')[0].id
        orders = order.objects.get(user=request.user, status='INCART', id=prodId)
    else:
        orders = order.objects.get(user=request.user, status='INCART')
    prodJson = ast.literal_eval(orders.prodJson)
    for key, value in prodJson.items():
        if product.objects.get(id=key).discount:
            totals.append(idtotal(key, value))
        else:
            withoutpercent.append(idtotal(key, value))
    carttotal = round(sum(totals), 3)
    if userdetail.objects.filter(user=request.user).exists():
        percent = userdetail.objects.filter(user=request.user)[0].OnCashPercentage
    else:
        percent = 0
    saved = round((float(carttotal) / 100 * float(percent)), 3)
    total = round(float(carttotal) - float(saved), 3)
    orders.carttotal = round(float(carttotal) + float(sum(withoutpercent)), 3)
    orders.percent = percent
    orders.saved = round(float(saved) + float(sum(withoutpercent)), 3)
    orders.total = round(float(total) + float(sum(withoutpercent)), 3)
    orders.save()
    return round(float(total) + float(sum(withoutpercent)), 3)
















#####################---------- Start Confrim Checkout Page Function ----------#####################
def confirmcheckout(request):
    payment = request.POST['payment']
    if payment == 'CREDIT':
        if len(list(order.objects.filter(user=request.user, status='INCART'))) > 1:
            prodId = order.objects.filter(user=request.user, status='INCART')[0].id
            ordersed = order.objects.get(user=request.user, status='INCART', id=prodId)
        else:
            ordersed = order.objects.get(user=request.user, status='INCART')
        ordersed.status = "PENDING"
        ordersed.payment = payment
        ordersed.orderDateTime = datetime.now()
        ordersed.save()
        userdetails = userdetail.objects.get(user=request.user)
        userdetails.total = round(float(userdetails.total) + float(ordersed.total), 3)
        userdetails.save()
        return JsonResponse({'data': True}, safe=False)
    elif payment == 'CASH':
        total = changetotal(request)
        if len(list(order.objects.filter(user=request.user, status='INCART'))) > 1:
            prodId = order.objects.filter(user=request.user, status='INCART')[0].id
            ordersed = order.objects.get(user=request.user, status='INCART', id=prodId)
        else:
            ordersed = order.objects.get(user=request.user, status='INCART')
        ordersed.status = "PENDING"
        ordersed.payment = payment
        ordersed.orderDateTime = datetime.now()
        ordersed.save()
        return JsonResponse({'data': 'true1', "total": total}, safe=False)
#####################---------- End Confrim Checkout Page Function ----------#####################






# context = {
#     'orders': ordersdef(request),
#     'favourite': favdef(request),
#     'brands': branddef(),
#     "categorys": categorydef(),
#     'colors': colordef(),

# #     Additional
#     'products': proddef(),
# }