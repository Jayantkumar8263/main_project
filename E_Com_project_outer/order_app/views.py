from django.shortcuts import render,redirect
from order_app.models import order_details, return_order
# Create your views here.

def ord_view(request):
    a = order_details.objects.all().order_by ('-id')
    if request.method == 'POST':
        order_no = request.POST.get('order_no')
        user_id = request.POST.get('user_id')
        product = request.POST.get('product')
        total_prise = request.POST.get('total_price')
        payment =request.POST.get('payment')
        shypping_address = request.POST.get('shypping_address')
        order_status = request.POST.get('order_status')
         
        if order_no:
            order_details.objects.create(order_no = order_no, user_id = user_id, product = product, total_prise = total_prise, payment = payment, shypping_address = shypping_address, order_status = order_status)
            return redirect('pro_home')
    return render(request, 'pro_home.html', {'key' : a})

def ord_update(request , id):
    data = order_details.objects.get(pk = id)
    
    if request.method == "POST":
        order_no = request.POST.get('order_no')
        user_id = request.POST.get('user_id')
        product = request.POST.get('product')
        total_prise = request.POST.get('total_price')
        payment =request.POST.get('payment')
        shypping_address = request.POST.get('shypping_address')
        order_status = request.POST.get('order_status')
        if order_no and user_id and product and total_prise and payment and shypping_address and order_status :
            
            data.order_no = order_no
            data.user_id = user_id
            data.product = product
            data.payment = payment
            data.shypping_address = shypping_address
            data.total_prise = total_prise
            data. order_status =  order_status
            data.save()
            return redirect('home')
    return render(request, 'index.html', {'key' : data})

def return_ord_view(request, id):
    data = return_order.objects.get(pk = id)
    
    if request.method == "POST":
        order_no = request.POST.get('order_no')     
        reason_for_return = request.POST.get('reason_for_return')
        
        if order_no and reason_for_return :
            data.order_no = request.POST.get('order_no')
            data.reason_for_return = request.POST.get('reason_for_return')
            data.save()
            return redirect('home')
    return render(request, 'return_order,html', {'key' : data})
    
def ord_card(request, id ):
    data = order_details.objects.get(pk = id, null = True, blank = True)
    data.save()
    return redirect('ord.html')