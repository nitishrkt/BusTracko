from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Wallet
from geopy.geocoders import GoogleV3

# geolocator = GoogleV3()
# location = geolocator.geocode("kharar")
# print(location.address)
# print((location.latitude, location.longitude))

# Create your views here.
def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pwd = request.POST['password']
        repwd = request.POST['repassword']
        print(username, fname, lname, email, pwd)
        if pwd == repwd:
            user = User.objects.create_user(username, email, pwd)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "Sign Up successful")
            return render(request, 'home.html')
        else:
            messages.danger(request, "Sign Up unsuccessful")
            return render(request, 'home.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return render(request,'mappage.html')
        else:
            return redirect('home')


def logoutpage(request):
    logout(request)
    return redirect('home')


def loginapp(request):
    if request.method == 'POST':
        userapp = request.POST['userapp']
        userpass = request.POST['userpass']
        user = authenticate(username = userapp, password = userpass)
        if user is not None:
            usermoney = Wallet.objects.filter(username=user).values()
            dictionary = usermoney[0]
            userbal = dictionary['balance']
            login(request, user)
            return render(request, 'wallet.html', {'username':user,'balance':userbal})


def AddMoney(request):
    if request.method == 'POST':
        money = request.POST['money']
        uservalue="nitishrkt"
        usermoney= Wallet.objects.filter(username__icontains=uservalue).values()
        dictionary = usermoney[0] 
        a = dictionary['balance']
        final_money = a + int(money)
        Wallet.objects.filter(username__icontains=uservalue).update(balance=final_money)
        return render(request,'wallet.html',{'username':"nitishrkt",'balance':final_money})


def MoneyDeduct(request):
    pass