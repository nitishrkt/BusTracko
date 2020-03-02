from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def handlemap(request):
    return render(request,'mappage2.html')
