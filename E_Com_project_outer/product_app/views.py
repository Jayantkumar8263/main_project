from django.shortcuts import render, redirect
from product_app.models import product_details, add_to_cart, buy_now
# Create your views here.

def pro_home(request, id):
    a = product_details.objects.get(pk=id)
    #  if request.method == "POST":
    #      name = request.POST.get('name')
    #      price = request.POST.get('price')
    #      quantity = request.POST.get('quantity')
    #      description = request.POST.get('description')
    #      descount_price = request.POST.get('descount_price')
    #      descount_percent = request.POST.get('descount_percent')
    #      on_scale = request.POST.get('on_scale')
    #      images = request.POST.get('images')
        
    #      if name:
    #          product_details.objects.create(name = name, price = price,quantity = quantity, description = description, descount_price = descount_price, descount_percent = descount_percent, on_scale = on_scale, images = images)
    #          return redirect('pro_home')
    return render(request, 'pro_home.html', {'key' : a})

def del_a(request, id):
    a = product_details.objects.get(pk = id)
    a.delete()
    return redirect('pro_home')

def up_a(request, id):
    a = product_details.objects.get(pk = id)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        descount_price = request.POST.get('descount_price')
        descount_percent = request.POST.get('descount_percent')
        on_scale = request.POST.get('on_scale')
        images = request.POST.get('images')
        if name :
            a.name = name
            a.price = price
            a.quantity = quantity
            a.description = description
            a.descount_price = descount_price
            a.descount_percent = descount_percent
            a.on_scale = on_scale
            a.images = images 
            a.save()
            return redirect('pro_home')
        
    return render(request, 'pro_home.html', {'key' : a})

# def card(request, id ):
#     a = product_details.objects.get(pk = id, null = True, blank = True)
#     a.save()
#     return redirect('pro.html')

def cart(request, id):
    user = request.user
    product = product_details.objects.get(id = id)
    add_to_cart.objects.create(user = user, product = product)
    return redirect('home')

def view_cart(request):
    user = request.user
    obj = add_to_cart.objects.filter(user = user)
    return render(request, 'view_cart.html',{"data" : obj})

def buy_now(request):
    user = request.user
    obj = add_to_cart.objects.filter(user = user)
    for i in obj :
        buy_now.objects.create(user= i.user, product = i.product)
        
    obj.delete()
    return redirect('home')
