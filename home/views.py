from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
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
            return HttpResponse('successful')
        else:
            return render(request, 'home.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login successful')
        else:
            return redirect('home')


def logoutpage(request):
    logout(request)
    return redirect('home')