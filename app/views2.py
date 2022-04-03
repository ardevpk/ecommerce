from django.http import HttpResponse, HttpResponseNotAllowed
from .views import idtotal
from .models import order, product
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  
import ast
from django.shortcuts import redirect


def pdf(request, id):
    template_path = '../templates/customer/order/pdf.html'
    if not request.user.is_authenticated:
        return redirect('/signin/')
    if not order.objects.filter(user=request.user, status="PENDING", id=id).exists():
        return HttpResponseNotAllowed('You Are Not Allowed To View This Pdf')
    ordersed = order.objects.filter(user=request.user, status="PENDING", id=id)[0]
    products = []
    prodQuan = []
    totals = []
    perproducts = []
    orderJson = ast.literal_eval(ordersed.prodJson)
    for key, value in orderJson.items():
        products.append(product.objects.filter(id=key)[0])
        prodQuan.append(value)
        totals.append(idtotal(key, value))
        perproducts.append(round(product.objects.filter(id=key)[0].priceByBox / product.objects.filter(id=key)[0].peicePerBox, 3))

    context = {
        "order": ordersed,
        "request": request,
        "products": products,
        "prodQuan": prodQuan,
        "perproducts": perproducts,
        "totals": totals}
    template = get_template(template_path)
    html  = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse("Something Went Wrong Please Contact Website Owner")