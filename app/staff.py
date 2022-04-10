from django.shortcuts import render, redirect
from django.contrib import messages
from .models import order, RECOVERY, RETURNS, userdetail
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()





def staffpending(request):
    if request.user.is_authenticated and request.user.is_staff:
        if order.objects.filter(status='PENDING').exists():
            orderdetails = order.objects.filter(status='PENDING').order_by("-orderDateTime")
        else:
            orderdetails = None
        context = {
            "orderdetails": orderdetails,
        }
        return render(request, "staff/pending.html", context)
    else:
        messages.add_message(request, messages.ERROR, 'You Don\'t Have Staff Authorities To Access This Page')
        return redirect('/signin/')





def staffprocessing(request):
    if request.user.is_authenticated and request.user.is_staff:
        if order.objects.filter(status='PROCESSING').exists():
            orderdetails = order.objects.filter(status='PROCESSING').order_by("-orderDateTime")
        else:
            orderdetails = None
        context = {
            "orderdetails": orderdetails,
        }
        return render(request, "staff/processing.html", context)
    else:
        messages.add_message(request, messages.ERROR, 'You Don\'t Have Staff Authorities To Access This Page')
        return redirect('/signin/')




def staffcompleted(request):
    if request.user.is_authenticated and request.user.is_staff:
        if order.objects.filter(status='COMPLETED').exists():
            orderdetails = order.objects.filter(status='COMPLETED').order_by("-orderDateTime")
        else:
            orderdetails = None
        context = {
            "orderdetails": orderdetails,
        }
        return render(request, "staff/completed.html", context)
    else:
        messages.add_message(request, messages.ERROR, 'You Don\'t Have Staff Authorities To Access This Page')
        return redirect('/signin/')




def staffcancelled(request):
    if request.user.is_authenticated and request.user.is_staff:
        if order.objects.filter(status='CANCELLED').exists():
            orderdetails = order.objects.filter(status='CANCELLED').order_by("-orderDateTime")
        else:
            orderdetails = None
        context = {
            "orderdetails": orderdetails,
        }
        return render(request, "staff/cancelled.html", context)
    else:
        messages.add_message(request, messages.ERROR, 'You Don\'t Have Staff Authorities To Access This Page')
        return redirect('/signin/')









def recovery(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == "POST":
            user = request.POST['user']
            cash = request.POST['cash']
            orderid = request.POST['orderid']
            receipt = request.FILES['receipt'] if "receipt" in request.FILES else None
            recoverys = RECOVERY.objects.create(user=User.objects.get(id=int(user)), cash=cash, orderid=orderid, image=receipt, recoveryBy=request.user, date=datetime.now())
            recoverys.save()
            userdetails = userdetail.objects.get(user=User.objects.get(id=int(user)))
            userdetails.total = round(float(userdetails.total) - float(cash), 3)
            userdetails.save()
            messages.add_message(request, messages.ERROR, 'Recovery Successful')
        context = {
            "users": User.objects.filter(is_staff=False),
        }
        return render(request, "staff/recovery.html", context)
    else:
        messages.add_message(request, messages.ERROR, 'You Don\'t Have Staff Authorities To Access This Page')
        return redirect('/signin/')







def returns(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == "POST":
            user = request.POST['user']
            cash = request.POST['cash']
            orderid = request.POST['orderid']
            receipt = request.FILES['receipt'] if "receipt" in request.FILES else None
            returnss = RETURNS.objects.create(user=User.objects.get(id=int(user)), cash=cash, orderid=orderid, image=receipt, returnTakenBy=request.user, date=datetime.now())
            returnss.save()
            userdetails = userdetail.objects.get(user=User.objects.get(id=int(user)))
            userdetails.total = round(float(userdetails.total) - float(cash), 3)
            userdetails.save()
            messages.add_message(request, messages.ERROR, 'Return Successful')
        context = {
            "users": User.objects.filter(is_staff=False),
        }
        return render(request, "staff/return.html", context)
    else:
        messages.add_message(request, messages.ERROR, 'You Don\'t Have Staff Authorities To Access This Page')
        return redirect('/signin/')




def changesaffstats(request, id, name):
    if request.user.is_authenticated and request.user.is_staff:
        orders = order.objects.get(id=id)
        orders.status = name
        if name == "COMPLETED":
            orders.CheckedBy = request.user
            orders.CheckedDate = datetime.now()
            print(orders.payment)
            if orders.payment == 'CREDIT':
                userdetails = userdetail.objects.get(user=orders.user)
                userdetails.total = round(float(userdetails.total) + float(orders.total), 3)
        orders.save()
        messages.add_message(request, messages.ERROR, 'Status Changed Successfully')
        return redirect('/staff/pending/')
    else:
        messages.add_message(request, messages.ERROR, 'You Don\'t Have Staff Authorities To Access This Page')
        return redirect('/signin/')