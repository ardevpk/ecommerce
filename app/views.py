from http.client import HTTPResponse
from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import render, redirect
from allauth.account.admin import EmailAddress
from django.contrib.auth.decorators import login_required
from .models import product, order, favourite
from django.contrib import messages
import json
import ast


# Create your views here.
@login_required(login_url='/signin/', redirect_field_name=None)
def index(request):
    if (request.user.is_verified or EmailAddress.objects.filter(email=request.user.email)[0].verified):
        products = product.objects.all().order_by('category')
        orders = order.objects.filter(by=request.user, status='INCART')
        brands = product.objects.values_list('brand', flat=True).distinct()
        context = {
            'orders': [orders] if orders else None,
            'products': products,
            'favourite': [favourite.objects.filter(user=request.user, added=values.added)[0].added for values in favourite.objects.filter(user=request.user)],
            'brands': brands,
        }
        return render(request, 'index.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Your Account Is Not Verified Yet Please Check Your Mail Or Contact Website Owner')
        return redirect('/signin/')



def idtotal(x, value):
    price = product.objects.get(id=x).priceByBox
    piece = product.objects.get(id=x).peicePerBox
    return int((int(price) / int(piece)) * int(value))

@login_required(login_url='/signin/', redirect_field_name=None)
def cart(request):
    if (request.user.is_verified or EmailAddress.objects.filter(email=request.user.email)[0].verified):
        orders = order.objects.filter(by=request.user, status='INCART')
        if not order.objects.filter(by=request.user, status='INCART').exists():
            return render(request, 'customer/cart.html', {'orders': [orders] if orders else None,})
        orderJson = ast.literal_eval(orders[0].prodJson)
        prodQuan = []
        products = []
        totals = []
        if orders:
            for key, value in orderJson.items():
                products.append(product.objects.get(id=key))
                totals.append(idtotal(key, value))
                prodQuan.append(value)
        context = {
            'orders': [orders] if orders else None,
            'products': products,
            'favourite': [favourite.objects.filter(user=request.user, added=values.added)[0].added for values in favourite.objects.filter(user=request.user)],
            'prodQuan': prodQuan,
            'totals': totals,
        }
        return render(request, 'customer/cart.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Your Account Is Not Verified Yet Please Check Your Mail Or Contact Website Owner')
        return redirect('/signin/')


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


def stafforders(request):
    return render(request, 'staff/stafforders.html')




def addtofav(request):
    data = int(request.POST.get('id'))
    if not favourite.objects.filter(user=request.user, added=int(data)).exists():
        favourite.objects.create(user=request.user, added=int(data))
        return JsonResponse({"data": True}, safe=False)
    else:
        favourite.objects.filter(user=request.user, added=int(data)).delete()
        return JsonResponse({"data": False}, safe=False)


def favouriteproducts(request):
	data = {
		"form_list": product.objects.all(),
        'favourite': [favourite.objects.filter(user=request.user, added=values.added)[0].added for values in favourite.objects.filter(user=request.user)],
	}
	return render(request, "customer/favourite.html", data)





@login_required(login_url='/signin/', redirect_field_name=None)
def productspage(request):
    if (request.user.is_verified or EmailAddress.objects.filter(email=request.user.email)[0].verified):
        products = product.objects.all().order_by('category')
        brands = product.objects.values_list('brand', flat=True).distinct()
        context = {
            'products': products,
            'favourite': [favourite.objects.filter(user=request.user, added=values.added)[0].added for values in favourite.objects.filter(user=request.user)],
            'brands': brands,
        }
        return render(request, 'customer/products.html', context)
    else:
        messages.add_message(request, messages.ERROR, 'Your Account Is Not Verified Yet Please Check Your Mail Or Contact Website Owner')
        return redirect('/signin/')