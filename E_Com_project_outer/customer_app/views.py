from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from customer_app.models import custom_user
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'home.html', {"form":form})
#for registration
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully.')
            return redirect('login')
    else:
         form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})   
#for login
def ulogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, name = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'invalid username or password')
    return render(request, 'login.html')
#for logout
def ulogout(request):
    logout(request)
    return redirect('home')
#for profile
def profile(request, i):
    user = User.objects.get(pk = i)
    return render(request, 'profile.html', {'user' : user})

def delete_data(request , id):
    data = custom_user.objects.get(pk = id)
    data.delete()
    return redirect('home')

def update_data(request , id):
    data = custom_user.objects.get(pk = id)
    if request.method == "GET":
        name = request.GET.get('name')
        email = request.GET.get('email')
        mobile = request.GET.get('mobile')
        address = request.GET.get('Address')
        if name and email and mobile and address: 
            data.name = name
            data.mobile = mobile
            data.address = address
            data.email = email
            data.save()
            return redirect('home')
    return render(request, 'index.html', {'key' : data})

def bank_details(request, id):
    data = custom_user.objects.get(pk = id)
    if request.method == 'GET':
        account = request.GET.get('account')
        bank_name = request.GET.get('bank_name')
        IFSC = request.GET.get('IFSC') 
        if account and bank_name and IFSC :
            data.account = account
            data.bank_name = bank_name
            data.IFSC = IFSC
            data.save()
            return redirect('home')
    return render(request, 'bank_det.html', {'key' : data})
    