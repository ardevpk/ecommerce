from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from allauth.account.admin import EmailAddress
from django.contrib.auth.decorators import login_required
from .models import product, order, favourite
from django.contrib import messages
import json
import ast




#####################---------- Start HelpFull Functions ----------#####################
def ordersdef(request):
    ordersed = order.objects.filter(by=request.user, status='INCART')
    return [ordersed] if ordersed else None


def favdef(request):
    fav = [favourite.objects.filter(user=request.user, added=values.added)[0].added for values in favourite.objects.filter(user=request.user)]
    return fav


def proddef():
    prod = product.objects.all().order_by('category')
    return prod

def branddef():
    brands = product.objects.values_list('brand', flat=True).distinct()
    return brands

def categorydef():
    categorys = product.objects.values_list('category', flat=True).distinct()
    return categorys



def checkuser(request):
    dicts = {}
    if EmailAddress.objects.filter(email=request.user.email).exists():
        if (request.user.is_verified or EmailAddress.objects.filter(email=request.user.email)[0].verified) and not request.user.is_staff:
            return dicts
        elif (request.user.is_verified or EmailAddress.objects.filter(email=request.user.email)[0].verified) and request.user.is_staff:
            dicts['url'] = '/signin/'
            return dicts
        else:
            messages.add_message(request, messages.ERROR, 'Your Account Is Not Verified Yet Please Check Your Mail Or Contact Website Owner')
            dicts['url'] = '/signin/'
            return dicts
    elif not EmailAddress.objects.filter(email=request.user.email).exists():
        if (request.user.is_verified) and not request.user.is_staff:
            return True
        elif (request.user.is_verified) and request.user.is_staff:
            dicts['url'] = '/signin/'
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
    return int((int(price) / int(piece)) * int(value))
#####################---------- End HelpFull Functions ----------#####################









#####################---------- Start Index Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def index(request):
    dicts = checkuser(request)
    if not 'url' in dicts:
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
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
        if not order.objects.filter(by=request.user, status='INCART').exists():
            return render(request, 'customer/cart.html', {
                'orders': ordersdef(request),
                'favourite': favdef(request),
                'brands': branddef(),
                "categorys": categorydef(),
                })
        orders = order.objects.filter(by=request.user, status='INCART')
        orderJson = ast.literal_eval(orders[0].prodJson)
        prodQuan = []
        products = []
        totals = []
        if orders:
            for key, value in orderJson.items():
                products.append(product.objects.filter(id=key)[0])
                totals.append(idtotal(key, value))
                prodQuan.append(value)
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            'products': products,
            'prodQuan': prodQuan,
            'totals': totals,
        }
        return render(request, 'customer/cart.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Cart Function ----------#####################




#####################---------- Start Fav Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def favouriteproducts(request):
    dicts = checkuser(request)
    if not 'url' in dicts:
        context = {
            'orders': ordersdef(request),
            'favourite': favdef(request),
            'brands': branddef(),
            "categorys": categorydef(),
            }
        return render(request, "customer/favourite.html", context)
    else:
        return redirect(dicts['url'])
#####################---------- End Fav Function ----------#####################





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
            'products': proddef(),
            }
        return render(request, 'customer/products.html', context)
    else:
        return redirect(dicts['url'])
#####################---------- End Product Page Function ----------#####################





#####################---------- Start Product From Cart Delete Function ----------#####################
@login_required(login_url='/signin/', redirect_field_name=None)
def delete(request, id):
    orders = order.objects.get(by=request.user, status='INCART')
    jsons = ast.literal_eval(orders.prodJson)
    if len(jsons) > 1:
        if str(id) in jsons.keys():
            del jsons[str(id)]
            orders.prodJson = jsons
            orders.save()
    else:
        orders.delete()
    return redirect('/cart/')
#####################---------- End Product From Cart Delete Function ----------#####################





























#---------------------------------On Json Call Functions---------------------------------#
#####################---------- Start Add Cart Function ----------#####################
def addcart(request):
    prodJson = {}
    prodId = request.POST.get('id')
    stock = int(product.objects.filter(id=prodId)[0].peicePerBox)
    prodquan = int(request.POST.get('quantity')) if not 'quantityb' in request.POST else int(int(request.POST.get('quantityb')) * int(stock))
    if not order.objects.filter(by=request.user, status='INCART').exists():
        prodJson[prodId] = prodquan
        createorder = order.objects.create(by=request.user, prodJson=prodJson)
        createorder.save()
    else:
        editorder = order.objects.filter(by=request.user, status='INCART')[0]
        prodJson = ast.literal_eval(editorder.prodJson)
        prodJson[prodId] = prodquan
        editorder.prodJson = prodJson
        editorder.save()
        return JsonResponse({'data': False}, safe=False)
    return JsonResponse({'data': True}, safe=False)
#####################---------- End Add Cart Function ----------#####################


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











# context = {
#     'orders': ordersdef(request),
#     'favourite': favdef(request),
#     'brands': branddef(),
#     "categorys": categorydef(),

# #     Additional
#     'products': proddef(),
# }