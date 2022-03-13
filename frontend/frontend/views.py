from urllib import response
from django.shortcuts import redirect, render
from backend.models import product
from backend.models import cart, checkout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout


def index(request):
    # params = product.objects.all()
    # tags = []
    # for i in product.objects.values_list('tag', flat=True):
    #     if i in tags:
    #         continue
    #     else:
    #         tags.append(i)
        
    # if cart.objects.filter(cartName=1).exists():
    # # if cart.objects.filter(cartName=request.user).exists():
    #     cartQuan = cart.objects.filter(cartName=request.user)
    # else:
    #     cartQuan = 0
    # print(request.headers['User-Agent'])
    # if request.method == 'POST':
    #     values = request.POST['quant']
    #     print(values)
    # return render(request, 'index.html', {'params': params, 'tags': tags, 'cQ':cartQuan})
    return render(request, 'index.html')



def products(request):
    params = product.objects.all()
    tags = []
    for i in product.objects.values_list('tag', flat=True):
        if i in tags:
            continue
        else:
            tags.append(i)
        
    if cart.objects.filter(cartName=request.user).exists():
        cartQuan = cart.objects.filter(cartName=request.user)
    else:
        cartQuan = 0
    return render(request, 'products.html', {'params': params, 'tags': tags, 'cQ':cartQuan})


def productref(request, slug):
    singleProduct = product.objects.filter(prodSlug=slug).first()
    return render(request, 'product.html', {'sP': singleProduct})


def Cart(request):
    # totalAmout = []
    # if cart.objects.filter(cartName=request.user).exists:
    #     cartDetail = cart.objects.filter(cartName=request.user)
    #     ext4 = cart.objects.values_list('perProdTotal', flat=True)
    #     for i in ext4:
    #         totalAmout.append(i)
    # else:
    #     cartDetail = 0
    
    # if totalAmout!=[]:
    #     tPay = int(sum(totalAmout)/100*90)
    # else:
    #     tPay = 0.00
    # if cart.objects.filter(cartName=1).exists():
    # # if cart.objects.filter(cartName=request.user).exists():
    #     cartQuan = cart.objects.filter(cartName=request.user)
    # else:
    #     cartQuan = 0
    # return render(request, 'cart.html', {'cD':cartDetail, 'tA':sum(totalAmout), 'tPay':tPay, 'cQ':cartQuan})
    return render(request, 'cart.html')


# @login_required(login_url='/login/')
def addCart(request, slug):
    detailsProduct = product.objects.get(id=slug)
    if request.method == 'POST':
        quant = request.POST['quant']
        if cart.objects.filter(prodId=slug).exists():
            pass
        else:
            carted = cart(cartName=request.user, prodId=slug, prodPrice=detailsProduct.price, prodTag=detailsProduct.tag, prodName=detailsProduct.name, prodImage=detailsProduct.image, prodQuan=quant, perProdTotal=detailsProduct.price*1)
            carted.save()
    else:
        if cart.objects.filter(prodId=slug).exists():
            pass
        else:
            carted = cart(cartName=request.user, prodId=slug, prodPrice=detailsProduct.price, prodTag=detailsProduct.tag, prodName=detailsProduct.name, prodImage=detailsProduct.image, prodQuan=1, perProdTotal=detailsProduct.price*1)
            carted.save()

    headerszs = request.META['HTTP_REFERER']
    header2 = str(headerszs).split('/')[-2]
    if header2 == 'products':
        return redirect('/products/')
    else:
        return redirect('/')


def quanInc(request, slug):
    quanIncrease = cart.objects.get(id=slug)
    quanIncrease.prodQuan = quanIncrease.prodQuan + 1
    quanIncrease.perProdTotal = quanIncrease.prodQuan * quanIncrease.prodPrice
    quanIncrease.save()
    return redirect('/cart/')

def quanDec(request, slug):
    quanDecrease = cart.objects.get(id=slug)
    if quanDecrease.prodQuan > 1:
        quanDecrease.prodQuan = quanDecrease.prodQuan - 1
        quanDecrease.perProdTotal = quanDecrease.prodQuan * quanDecrease.prodPrice
        quanDecrease.save()
    return redirect('/cart/')


def prodDelete(request, slug):
    productDelete = cart.objects.get(id=slug)
    productDelete.delete()
    return redirect('/cart/')




def CHeckout(request):    
    totalAmout = []
    totalAmout1 = []
    totalAmout2 = []
    totalAmout3 = []
    if cart.objects.filter(cartName=request.user).exists():
        cartDetail = cart.objects.filter(cartName=request.user)
        ext4 = cart.objects.filter(cartName=request.user).values_list('perProdTotal', flat=True)
        ext5 = cart.objects.filter(cartName=request.user).values_list('prodName', flat=True)
        ext6 = cart.objects.filter(cartName=request.user).values_list('prodId', flat=True)
        ext7 = cart.objects.filter(cartName=request.user).values_list('prodQuan', flat=True)
        for i in ext4:
            totalAmout.append(i)
        for i in ext5:
            totalAmout1.append(i)
        for i in ext6:
            totalAmout2.append(i)
        for i in ext7:
            totalAmout3.append(i)
    else:
        cartDetail=0
    if totalAmout!=[]:
        tPay = int(sum(totalAmout)/100*90)
    else:
        tPay = 0.00
    if request.method == 'POST':
        yname = request.POST['yname']
        sname = request.POST['sname']
        phone = request.POST['phone']
        address = request.POST['address']
        aod = request.POST['aod']
        checkouted = checkout(checkoutName=request.user, yourName=yname, shopName=sname, phone=phone, address=address, aod=aod, toPay=tPay, checkoutProdName=totalAmout1, checkoutProdId=totalAmout2, checkoutProdQuan=totalAmout3)
        checkouted.save()
        for i in cartDetail:
            i.delete()
        return redirect('/')


    if cart.objects.filter(cartName=request.user).exists():
        cartQuan = cart.objects.filter(cartName=request.user)
    else:
        cartQuan = 0
    return render(request, 'checkout.html', {'tPay':tPay, 'cQ':cartQuan})



def recovery(request):
    if request.user.is_authenticated and request.user.is_staff:
        params = User.objects.all()
        data = {
            'params':params
        }
        return render(request, "recovery.html", data)
    else:
        return redirect('/')

def LogOut(request):
    logout(request)
    return redirect('/')